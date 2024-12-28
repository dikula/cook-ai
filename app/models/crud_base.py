from typing import Generic, Type, TypeVar, List, Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from pydantic import BaseModel
from sqlalchemy.inspection import inspect

# Type variables
ModelType = TypeVar("ModelType")  # SQLAlchemy dataclass model
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)  # Pydantic schema for creation
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)  # Pydantic schema for update


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object for SQLAlchemy dataclasses.

        :param model: A SQLAlchemy dataclass model
        """
        self.model = model

    def get(self, db: Session, id: int) -> Optional[ModelType]:
        """Get a single record by ID."""
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """Get multiple records with optional pagination."""
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        """Create a new record."""
        try:
            obj_data = obj_in.dict()  # Convert Pydantic schema to dict
            db_obj = self.model(**obj_data)  # Create a dataclass instance
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except IntegrityError:
            db.rollback()
        return {}

    def update(
        self, db: Session, db_obj: ModelType, obj_in: UpdateSchemaType
    ) -> ModelType:
        """Update an existing record."""
        try:
            obj_data = obj_in.dict(exclude_unset=True)  # Convert Pydantic schema to dict
            for field, value in obj_data.items():
                if hasattr(db_obj, field):
                    setattr(db_obj, field, value)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except IntegrityError:
            db.rollback()
        return {}

    # def delete(self, db: Session, id: int) -> Optional[ModelType]:
    #     """Delete a record by ID."""
    #     obj = db.query(self.model).filter(self.model.id == id).first()
    #     if obj:
    #         db.delete(obj)
    #         db.commit()
    #     return obj
