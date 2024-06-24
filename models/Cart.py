from models.base_model import Base
from sqlalchemy import Column, Integer, ForeignKey

class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('menu_items.id'), nullable=False)
    quantity = Column(Integer, default=1)
