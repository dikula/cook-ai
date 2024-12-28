from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema for creating a new user
class UserCreate(BaseModel):
    email: EmailStr
    password: str  # Plaintext password for demonstration (hash it in practice)


# Schema for reading a user (response)
class UserRead(BaseModel):
    id: Optional[int]
    email: Optional[EmailStr]
    password: Optional[str]
    is_active: Optional[bool]

    class Config:
        orm_mode = True


class UserEmail(BaseModel):
    email: EmailStr