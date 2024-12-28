from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserRead
from app.crud.user import CRUDUser
from app.schemas.user import UserEmail

# from app.crud.user_crud import get_users, get_user_by_id

router = APIRouter()
crud_user = CRUDUser(User)


@router.post("/user/register", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Create the new user record
    new_user = crud_user.create(
        db=db,
        obj_in=UserCreate(
            email=user.email,
            password=user.password,
        ),
    )
    return new_user


@router.get("/user/check-email")#, response_model=UserRead)
def get_user(user: UserEmail = Depends(), db: Session = Depends(get_db)):
    # Hash the password before saving (you can use Passlib for this)

    return {"exits": True if crud_user.get_by_email(db=db, email=user.email) else False}
