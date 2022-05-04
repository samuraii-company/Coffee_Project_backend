import os

from dotenv import load_dotenv

load_dotenv()

SECRET_TOKEN = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
