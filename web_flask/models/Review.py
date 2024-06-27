from main import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models

class Review(db.Model):
    """Representation of a review"""
    __tablename__ = 'reviews'
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comment = db.Column(db.String(1024), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))  # Assuming ForeignKey pointing to the restaurants table

    user = db.relationship("User", back_populates="reviews")

    def __init__(self, *args, **kwargs):
        """Initializes Review"""
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'Review(id={self.id}, user_id={self.user_id}, comment={self.comment})'
