from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.api.user import router as user_router
from app.api.cook import router as cook_router
# from database import SessionLocal, engine
# from .chatgpt import ask_chatgpt
# from api.user import router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router)
app.include_router(cook_router)

# print('SALALA', app.routes)
# for route in app.routes:
#     print('AAAAA',route)
#     if hasattr(route, "path"):
#         methods = getattr(route, "methods", ["GET"])
#         print(f"Path: {route.path}, Methods: {methods}")
