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
        _tablename_ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        phone_number = Column(String(20), nullable=True)
        address = Column(String(256), nullable=True)
        orders = relationship("Order", back_populates="user")
        cart = relationship("Cart", uselist=False, back_populates="user")
        
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        phone_number = ""
        address = ""
        cart = []

    def _init_(self, *args, **kwargs):
        """initializes user"""
        super()._init_(*args, **kwargs)

    def _setattr_(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super()._setattr_(name, value)