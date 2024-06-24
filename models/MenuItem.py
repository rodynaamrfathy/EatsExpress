from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    price = Column(Integer, nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
