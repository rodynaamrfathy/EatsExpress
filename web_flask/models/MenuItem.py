#!/usr/bin/python3
""" Definition of the MenuItem model """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey

class MenuItem(BaseModel, Base):
    """ Representation of a MenuItem """
    if models.storage_t == 'db':
        __tablename__ = 'menu_items'
        name = Column(String(128), nullable=False)
        price = Column(Integer, nullable=False)
        description = Column(String(256), nullable=True)
        restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)  # Foreign key to Restaurant
        carts = relationship("Cart", back_populates="menu_item")  # Relationship with Cart
    else:
        name = ""
        price = 0
        description = ""
        restaurant_id = ""
        carts = []

    def __init__(self, *args, **kwargs):
        """ Initializes the menu item """
        super().__init__(*args, **kwargs)
