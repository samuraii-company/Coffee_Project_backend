from restapi.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from restapi.coffee.models import Coffee
from restapi.users.models import Users
from datetime import datetime


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    client = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    telegram_charge_id = Column(String(200))
    payment_charge_id = Column(String(200))
    coffee = Column(Integer, ForeignKey("coffee.id", ondelete="CASCADE"))
    status = Column(String(30), default="PENDING")
    order_number = Column(Integer)
    order_price = Column(Integer)
    client_info = relationship(Users, back_populates="orders")
    coffee_info = relationship(Coffee, back_populates="orders")
    ordered_by = Column(DateTime, default=datetime.now)
