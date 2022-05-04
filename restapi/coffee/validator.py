from sqlalchemy.orm import Session
from . import models


async def unique_coffee_name(coffee_title: str, database: Session):
    """Validate what coffee with this name already exists in system"""

    return database.query(models.Coffee).filter(models.Coffee.title == coffee_title).first()
