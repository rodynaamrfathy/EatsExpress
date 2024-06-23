# models/review.py

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """Representation of a review"""
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    #rating = Column(Integer, nullable=False)
    comment = Column(String(1024), nullable=True)
    user = relationship("User", back_populates="reviews")
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))  # ForeignKey pointing to the restaurants table
    content = Column(String(500), nullable=True)