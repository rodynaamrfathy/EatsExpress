import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Float, Table,Integer,ForeignKey
from sqlalchemy.orm import relationship 

class Cart(Base):
    if models.storage_t == 'db':
        __tablename__ = 'cart'
        user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
        item_id = Column(Integer, ForeignKey('menu_items.id'), nullable=False)
        quantity = Column(Integer, default=1)

    else:
        user_id = ""
        item_id = ""
        quantity = 0
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if models.storage_t != 'db':
        
            @property
            def products(self):
                """getter attribute returns the list of Product instances"""
                from models.Cart import cart
                product_list = []
                all_products = models.storage.all(Cart)
                for product in all_products.values():
                    if product.order_id == self.id:
                        product_list.append(Cart)
                return product_list
