#!/usr/bin/python3
""" Definition of the Restaurant model """

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Float, Table
from sqlalchemy.orm import relationship


class Restaurant(BaseModel, Base):
    """ Representation of a Restaurant """
    if models.storage_t == 'db':
        __tablename__ = 'restaurants'
        name = Column(String(128), nullable=False)
        location = Column(String(256), nullable=False)
        reviews = relationship("Review", backref="restaurant")
        delivery_time = Column(String(256), nullable=False)
        cuisines = Column(String(256), nullable=False)
        categories = Column(String(256), nullable=False)
        breakfast = Column(String(256), nullable=False)
        beverages = Column(String(256), nullable=False)
        image = Column(String)
        delivery_fee = Column(Float, nullable=False, default=0.0)
    else:
        name = ""
        location = ""
        delivery_time = 30 
        cuisines = ""
        categories = ""
        breakfast = ""
        beverages = ""
        image = ""
        delivery_fee = 10.0

    def __init__(self, *args, **kwargs):
        """ Initializes the restaurant """
        super().__init__(*args, **kwargs)