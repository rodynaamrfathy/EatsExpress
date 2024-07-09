# models/order.py

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Table, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

if models.storage_t == 'db':
    order_product = Table('order_product', Base.metadata,
                        Column('order_id', String(60), ForeignKey('orders.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
                        Column('product_id', String(60), ForeignKey('products.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True))


class Order(BaseModel, Base):
    """Representation of an order"""
    if models.storage_t == 'db':
         __tablename__ = 'orders'
         user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
         menu_items = relationship("MenuItem", backref="order")
         total_price = Column(Integer, nullable=False)
         user = relationship("User", back_populates="orders")
         restaurant_id = Column(String(60), ForeignKey('restaurants.id'), nullable=False)
         restaurant = relationship("Restaurant", back_populates="orders")
         address_id = Column(String(60), ForeignKey('addresses.id'), nullable=False)  # Changed to address_id
         delivery_time = Column(String(60), nullable=True)
         status = Column(String(60), nullable=True)
         
    else:
        user_id = ""
        total_price = 0
        menu_items = []
        restaurant_id = ""
        address_id = ""
        delivery_time = ""
        status = "none"

    def __init__(self, *args, **kwargs):
        """Initializes Order"""
        super().__init__(*args, **kwargs)