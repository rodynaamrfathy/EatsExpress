from app import db
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
        product_name = Column(String(128), nullable=False)
        quantity = Column(Integer, nullable=False)
        price = Column(Integer, nullable=False)
        user = relationship("User", back_populates="orders")

    else:

        user_id = ""
        product_name_name = ""
        quantity = ""
        price = 0
        products_ids = []

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