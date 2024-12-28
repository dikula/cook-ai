from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "postgresql+psycopg2://fastapi_user:fastapi_password@localhost:5440/fastapi_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
#
# import logging
# logging.basicConfig()
# logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
