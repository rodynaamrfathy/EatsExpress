# models/review.py

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
<<<<<<< HEAD
from sqlalchemy.orm import relationship
=======
from sqlalchemy.orm import relationship  # Import relationship
from models.user import User  # Ensure User is imported
>>>>>>> 3b8364c (s)

class Review(BaseModel, Base):
    """Representation of a review"""
    __tablename__ = 'reviews'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(1024), nullable=True)
    user = relationship("User", back_populates="reviews")