from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from fastapi.responses import JSONResponse
from typing import List

from sqlalchemy.orm import Session
from restapi.auth.jwt import get_stuff_user

from . import services
from . import schemas
from . import validator

from restapi.users.schemas import User

from restapi.db import get_db

router = APIRouter(tags=["coffee"], prefix="/api/v1/coffee")


@router.get("/", response_model=List[schemas.OutCoffeeSchemas])
async def get_all_coffee(database: Session = Depends(get_db)):
    """
    Get all coffee
    """
    coffee = await services.get_all_coffee(database)

    if not coffee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Coffee not found in the system",
        )

    return coffee


@router.post("/", response_model=schemas.CoffeeSchemas)
async def create_coffee(
    coffee: schemas.CoffeeSchemas, database: Session = Depends(get_db), current_user: User = Depends(get_stuff_user)
):
    """Create New Coffee"""

    _status = await validator.unique_coffee_name(coffee.title, database)

    if _status:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Coffee already exists in the system",
        )

    await services.create_new_coffee(coffee, database)

    return JSONResponse(status_code=201, content={"status": "coffee was created"})


@router.get("/{id}/", response_model=schemas.OutCoffeeSchemas)
async def get_coffee_by_id(id: int, database: Session = Depends(get_db)):
    """Get Coffee by id"""

    coffee = await services.get_coffee_by_id(id, database)
    if not coffee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Coffee with this id not found in system",
        )
    return coffee


@router.delete("/{id}/", status_code=200)
async def get_coffee_by_id(id: int, database: Session = Depends(get_db), current_user: User = Depends(get_stuff_user)):
    """Delete Coffee by id"""

    if not await services.get_coffee_by_id(id, database):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Coffee with this id not found in system",
        )

    await services.delete_coffee_by_id(id, database)

    return JSONResponse(status_code=200, content={"status": "coffee was deleted"})
