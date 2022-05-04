from typing import Optional, List
from sqlalchemy.orm import Session
from . import models
from . import schemas


async def get_all_coffee(database: Session) -> Optional[List[models.Coffee]]:
    """Return all coffee from database"""

    return database.query(models.Coffee).all()


async def create_new_coffee(coffee: schemas.CoffeeSchemas, database: Session):
    """Insert new coffee in database"""

    new_coffee = models.Coffee(
        title=coffee.title, description=coffee.description, price=coffee.price, image_url=coffee.image_url
    )

    database.add(new_coffee)
    database.commit()
    database.refresh(new_coffee)


async def get_coffee_by_id(id: int, database: Session):
    """Get coffee by id"""

    return database.query(models.Coffee).filter(models.Coffee.id == id).first()


async def delete_coffee_by_id(id: int, database: Session):
    """Delete coffee by id"""

    database.query(models.Coffee).filter(models.Coffee.id == id).delete()
    database.commit()
