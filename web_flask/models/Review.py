# models/review.py

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Review(BaseModel, Base):
    """Representation of a review"""
    if models.storage_t == 'db':
    
        __tablename__ = 'reviews'
        user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
        comment = Column(String(1024), nullable=True)
        restaurant_id = Column(Integer, ForeignKey('restaurants.id'))  # ForeignKey pointing to the restaurants table

    else:
        user_id = ""
        comment = ""


    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)