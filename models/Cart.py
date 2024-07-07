import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

class Cart(BaseModel, Base):
    if models.storage_t == 'db':
        __tablename__ = 'carts'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        restaurant_id = Column(String(60), ForeignKey('restaurants.id'), nullable=False)
        menu_items = relationship("MenuItem", backref="cart")

    else:
        user_id = ""
        restaurant_id = ""
        menu_items = []

    def __init__(self, *args, **kwargs):
        """ Initializes the cart """
        super().__init__(*args, **kwargs)
        self.menu_items = []

    def add_item(self, menu_item_id, menu_item_name, quantity, price):
        item = next((item for item in self.menu_items if item['id'] == menu_item_id), None)
        if item:
            item['quantity'] += quantity
            item['price'] = item['quantity'] * price
        else:
            self.menu_items.append({
                'id': menu_item_id,
                'name': menu_item_name,
                'quantity': quantity,
                'price': quantity * price
            })
