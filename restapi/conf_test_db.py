from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from restapi.db import Base, get_db
from main import app

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:secretpassword@127.0.0.1:5432/test_coffeedb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
