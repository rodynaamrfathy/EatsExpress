from main import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(db.Model):
    """Representation of a user"""
    __tablename__ = 'users'
    
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=True)
    last_name = db.Column(db.String(128), nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(256), nullable=True)

    def __repr__(self):
        return f'person with name {self.first_name} and email {self.email}'
