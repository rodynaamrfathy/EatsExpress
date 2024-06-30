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
        user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
        menu_items = relationship("MenuItem", backref="order")
        Total = Column(Integer, nullable=False)
        user = relationship("User", back_populates="order")
        restaurant_id =  Column(Integer, ForeignKey('restaurant.id'), nullable=False)
        restaurant = relationship("Restaurant", back_populates="order")

       
    else:
        user_id = ""
        Total = ""
        menu_items = []
        restaurant_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Order"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        
        @property
        def products(self):
            """getter attribute returns the list of Product instances"""
            from models.Restaurant import Restaurant
            product_list = []
            all_products = models.storage.all(Restaurant)
            for product in all_products.values():
                if product.order_id == self.id:
                    product_list.append(Restaurant)
            return product_list