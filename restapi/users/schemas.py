from pydantic import BaseModel

from typing import Optional


class User(BaseModel):
    id: Optional[int]
    telegram_id: int
    email: str
    password: str
    is_stuff: Optional[bool] = False

    class Config:
        schema_extra = {"example": {"telegram_id": 55564345, "email": "test@example.com", "password": "password"}}


class OutUser(BaseModel):
    id: int
    telegram_id: int
    email: str
    is_stuff: Optional[bool] = False

    class Config:
        orm_mode = True
        schema_extra = {"example": {"id": 1, "telegram_id": 55564345, "email": "test@example.com", "is_stuff": False}}
