from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class User(Base):
    __tablename__ = "tbl_user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
