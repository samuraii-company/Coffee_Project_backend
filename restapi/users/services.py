from sqlalchemy.orm import Session
from . import models
from . import schemas

from restapi.auth import hashing


async def new_user_register(user: schemas.User, database: Session):
    """Create new user"""

    _user = models.Users(
        email=user.email, telegram_id=user.telegram_id, password=hashing.get_password_hash(user.password)
    )

    database.add(_user)
    database.commit()
    database.refresh(_user)


async def get_all_coffee(database: Session):
    """Get all users"""

    return database.query(models.Users).all()
