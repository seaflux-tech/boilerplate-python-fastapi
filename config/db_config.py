# Importing libraries
from sqlalchemy import MetaData
from sqlalchemy.engine import create_engine
import os
from sqlalchemy.orm import sessionmaker

# Initialization
metadata = MetaData()

# Creating engine
auth = f"{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}"
engine = create_engine(
    f"postgresql://{auth}@{os.getenv('DATABASE_URL')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}",
    pool_recycle=3600,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Connecting db
with engine.connect() as db:
    metadata.reflect(db)