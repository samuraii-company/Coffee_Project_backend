from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from restapi.users.schemas import OutUser
from restapi.coffee.schemas import OutCoffeeSchemas


class OrderSchemas(BaseModel):
    payment_charge_id: str
    telegram_charge_id: str
    client: int
    coffee: int
    order_number: int
    order_price: int

    class Config:
        schema_extra = {
            "example": {
                "telegram_charge_id": "2076523459_535590856_108052",
                "payment_charge_id": "2a020b19-000f-5000-8000-12bf6af1050c",
                "client": 1,
                "coffee": 1,
                "order_number": 6821,
                "order_price": 400,
            }
        }


class OutOrderSchema(BaseModel):
    id: int
    payment_charge_id: str
    telegram_charge_id: str
    client_info: OutUser
    coffee_info: OutCoffeeSchemas
    order_number: int
    order_price: int
    ordered_by: Optional[datetime]
    status: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "payment_charge_id": "2a020b19-000f-5000-8000-12bf6af1050c",
                "telegram_charge_id": "2076523459_535590856_108052",
                "client_info": {"id": 1, "telegram_id": 55564345, "email": "test@example.com", "is_stuff": False},
                "coffee_info": {
                    "id": 1,
                    "title": "latte",
                    "description": "Latte Coffee",
                    "price": 250,
                    "image_url": "https://test.com/images/coffee.jpg",
                },
                "order_number": 6821,
                "order_price": 250,
                "ordered_by": "2022-05-03T21:54:25.735771",
                "status": "complited",
            }
        }


class UpdateStatusSchema(BaseModel):
    status: str

    class Config:
        orm_mode = True
        schema_extra = {"example": {"status": "delivery"}}
