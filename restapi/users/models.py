from restapi.db import Base

from sqlalchemy import BigInteger, Column, Integer, String, Boolean
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String(100))
    password = Column(String(100))
    telegram_id = Column(BigInteger)
    is_stuff = Column(Boolean, default=False)
    orders = relationship("Orders", back_populates="client_info")
