from main import db
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models

class Restaurant(db.Model):
    """ Representation of a Restaurant """
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(256), nullable=True)
    reviews = db.relationship("Review", backref="restaurant")

    def __init__(self, *args, **kwargs):
        """ Initializes the restaurant """
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'Restaurant(id={self.id}, name={self.name}, location={self.location})'
