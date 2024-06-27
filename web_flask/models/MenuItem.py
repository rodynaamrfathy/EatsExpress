from app import db
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey

class MenuItem(BaseModel, Base):
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
            """Getter attribute returns the list of Product instances"""
            from models.MenuItem import MenuItem
            product_list = []
            all_products = models.storage.all(MenuItem)
            for product in all_products.values():
                if product.order_id == self.id:
                    product_list.append(product)
            return product_list
