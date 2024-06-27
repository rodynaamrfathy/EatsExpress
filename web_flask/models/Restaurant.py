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
