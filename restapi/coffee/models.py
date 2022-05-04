from restapi.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Coffee(Base):
    __tablename__ = "coffee"

    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title: str = Column(String(100))
    description: str = Column(String(500))
    price: int = Column(Integer)
    image_url: str = Column(String(500))
    orders = relationship("Orders", back_populates="coffee_info")
