from app.database import Base, engine
from app.models.user import User

# Create all tables
print("Creating tables...")
Base.metadata.create_all(bind=engine)
# mapper_registry.metadata.create_all(bind=engine)
print("Tables created!")

