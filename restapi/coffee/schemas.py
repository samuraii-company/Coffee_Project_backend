from pydantic import BaseModel
from typing import Optional


class CoffeeSchemas(BaseModel):
    id: Optional[int]
    title: str
    description: str
    price: int
    image_url: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "title": "latte",
                "description": "Latte Coffee",
                "price": 250,
                "image_url": "https://test.com/images/coffee.jpg",
            }
        }


class OutCoffeeSchemas(BaseModel):
    id: int
    title: str
    description: str
    price: int
    image_url: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "latte",
                "description": "Latte Coffee",
                "price": 250,
                "image_url": "https://test.com/images/coffee.jpg",
            }
        }
