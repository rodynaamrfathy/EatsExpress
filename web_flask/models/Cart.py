from main import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Cart(db.Model):
    """Representation of a shopping cart item"""
    __tablename__ = 'cart'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('menu_items.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    
    user = db.relationship("User")  # Assuming User model exists
    item = db.relationship("MenuItem")  # Assuming MenuItem model exists

    def __repr__(self):
        return f'Cart(user_id={self.user_id}, item_id={self.item_id}, quantity={self.quantity})'
