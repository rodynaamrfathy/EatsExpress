#!/usr/bin/python3
""" Definition of the Restaurant model """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Restaurant(BaseModel, Base):
    """ Representation of a Restaurant """
    if models.storage_t == 'db':
        __tablename__ = 'restaurants'
        name = Column(String(128), nullable=False)
        location = Column(String(256), nullable=True)
        menu_items = relationship("MenuItem", backref="restaurant")  # One-to-many relationship with MenuItem

    else:
        name = ""
        location = ""

    def __init__(self, *args, **kwargs):
        """ Initializes the restaurant """
        super().__init__(*args, **kwargs)

        
    def to_dict(self):

        """Returns a dictionary representation of the restaurant"""
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'image_filename': self.image_filename,
            'delivery_fee': self.delivery_fee,
            'delivery_time': self.delivery_time,
            'tags': [{'name': tag.name} for tag in self.tags]
        }
