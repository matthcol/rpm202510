import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DB_URL", "").strip()

if DATABASE_URL:
    # Cas : base distante (Postgres, MySQL, etc.)
    engine = create_engine(DATABASE_URL, echo=True)
    should_create_db = False
else:
    # Cas : fallback SQLite local
    DATABASE_URL = "sqlite:///./local.db"
    engine = create_engine(
        DATABASE_URL,
        echo=True,
        connect_args={"check_same_thread": False}  # nécessaire pour SQLite
    )
    should_create_db = True

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
if should_create_db:
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
