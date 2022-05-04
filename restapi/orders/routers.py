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

from restapi.users.schemas import User

from restapi.db import get_db

router = APIRouter(tags=["orders"], prefix="/api/v1/orders")


@router.get("/", response_model=List[schemas.OutOrderSchema])
async def get_all_orders(database: Session = Depends(get_db), current_user: User = Depends(get_stuff_user)):
    """Get all orders"""

    orders = await services.get_all_orders(database)

    if not orders:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No One Order not found in the system",
        )

    return orders


@router.get("/{id}/", response_model=schemas.OutOrderSchema)
async def get_order_by_id(id: int, database: Session = Depends(get_db), current_user: User = Depends(get_stuff_user)):
    """Get Order by id"""

    order = await services.get_order_by_id(id, database)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order with this id not found in system",
        )
    return order


@router.post("/", response_model=schemas.OrderSchemas)
async def create_order(
    order: schemas.OrderSchemas, database: Session = Depends(get_db), current_user: User = Depends(get_stuff_user)
):
    """Create new order"""

    await services.create_order(order, database)

    return JSONResponse(status_code=201, content={"status": "Order was created"})


@router.patch("/{id}/", response_model=schemas.UpdateStatusSchema)
async def change_order_status(
    id: int,
    order_status: schemas.UpdateStatusSchema,
    database: Session = Depends(get_db),
    current_user: User = Depends(get_stuff_user),
):
    """Update order status by id"""

    order = await services.get_order_by_id(id, database)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order with this id not found in system",
        )

    await services.update_order_status(id, order_status, database)

    return JSONResponse(status_code=200, content={"status": "Status was updated"})
