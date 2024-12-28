from typing import Generic, Type, TypeVar
from sqlalchemy.orm import Session
from pydantic import BaseModel

ModelType = TypeVar("ModelType")  # SQLAlchemy model
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        obj_data = obj_in.dict()
        db_obj = self.model(**obj_data)  # Create SQLAlchemy model instance
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, id: int) -> ModelType | None:
        return db.query(self.model).filter(self.model.id == id).first()

    def list(self, db: Session, skip: int = 0, limit: int = 100) -> list[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

from app.models.user import User
from app.schemas.user import UserCreate


class CRUDUser(CRUDBase[User, UserCreate]):
    def get_by_email(self, db: Session, email: str) -> ModelType | None:
        return db.query(self.model).filter(self.model.email == email).first()