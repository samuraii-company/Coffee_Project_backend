from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from typing import List

from sqlalchemy.orm import Session
from restapi.auth.jwt import get_stuff_user
from . import services
from . import schemas
from . import validator

from restapi.users.schemas import User

from restapi.db import get_db

router = APIRouter(tags=["users"], prefix="/api/v1/users")


@router.get("/", response_model=List[schemas.OutUser])
async def get_all_users(database: Session = Depends(get_db), current_user: User = Depends(get_stuff_user)):
    """Get all users"""
    users = await services.get_all_coffee(database)

    return users


@router.get("/me/", response_model=schemas.OutUser)
async def get_info_about_user(
    q: int, database: Session = Depends(get_db), current_user: User = Depends(get_stuff_user)
):
    """Get info about user"""

    _user = await validator.verify_telegram_id_exist(q, database)

    if not _user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with this credentials not found in system",
        )

    return _user


@router.get("/user/exists/", status_code=status.HTTP_200_OK)
async def get_user_exists_status(q: int, database: Session = Depends(get_db)):
    """Returf True of False"""

    _user = await validator.verify_telegram_id_exist(q, database)

    if not _user:
        return False

    return True
