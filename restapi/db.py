from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from restapi.settings import config as cfg


db_name = cfg.DATABASE_NAME
db_host = cfg.DATABASE_HOST
db_port = cfg.DATABASE_PORT
db_username = cfg.DATABASE_USERNAME
db_password = cfg.DATABASE_PASSWORD

DATABASE_URL = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
