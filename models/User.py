#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """Representation of a user for EatExpress"""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        phone_number = Column(String(20), nullable=True)
        address = Column(String(256), nullable=True)
        orders = relationship("Order", back_populates="user")
        reviews = relationship("Review", back_populates="user")
        
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        phone_number = ""
        address = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
