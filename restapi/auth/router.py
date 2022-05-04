from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from restapi.auth import hashing
from restapi.users import models
from restapi.users import schemas
from restapi.users import validator
from restapi.users import services

from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .jwt import create_access_token
from restapi import db

router = APIRouter(tags=["auth"])


@router.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends(), database: Session = Depends(db.get_db)):
    """Login request"""

    user = database.query(models.Users).filter(models.Users.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Credentials")

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Password")

    access_token = create_access_token(data={"sub": user.email, "stuff": user.is_stuff})

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", response_model=schemas.User)
async def register(user: schemas.User, database: Session = Depends(db.get_db)):
    """Create New User"""
    _user_exists = await validator.verify_telegram_id_exist(user.telegram_id, database)
    if _user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this telegram id already exists in the system",
        )
    await services.new_user_register(user, database)

    return JSONResponse(status_code=201, content={"status": "user was created"})
