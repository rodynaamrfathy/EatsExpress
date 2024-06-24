import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Float, Table,Integer,ForeignKey
from sqlalchemy.orm import relationship 

class MenuItem(Base):
    if models.storage_t == 'db':
        __tablename__ = 'menu_items'
        name = Column(String(128), nullable=False)
        price = Column(Integer, nullable=False)
        restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)

    else:
        name = ""
        price = 0
        restaurant_id = ""

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)


    if models.storage_t != 'db':
        
                @property
                def products(self):
                    """getter attribute returns the list of Product instances"""
                    from models.MenuItem import MenuItem
                    product_list = []
                    all_products = models.storage.all(MenuItem)
                    for product in all_products.values():
                        if product.order_id == self.id:
                            product_list.append(MenuItem)
                    return product_list
