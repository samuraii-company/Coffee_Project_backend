from sqlalchemy.orm import Session

from . import models
from . import schemas


async def get_all_orders(database: Session):
    """Get all orders"""

    return database.query(models.Orders).all()


async def get_order_by_id(id: int, database: Session):
    """Get order by id"""

    return database.query(models.Orders).filter(models.Orders.id == id).first()


async def create_order(order: schemas.OrderSchemas, database: Session):
    """Insert new order"""

    new_order = models.Orders(
        client=order.client,
        telegram_charge_id=order.telegram_charge_id,
        payment_charge_id=order.payment_charge_id,
        coffee=order.coffee,
        order_number=order.order_number,
        order_price=order.order_price,
    )

    database.add(new_order)
    database.commit()
    database.refresh(new_order)


async def update_order_status(id: int, order: schemas.UpdateStatusSchema, database: Session):
    """Update order status in database"""
    _order = database.query(models.Orders).filter(models.Orders.id == id)

    _order.update({"status": order.status}, synchronize_session=False)
    database.commit()
