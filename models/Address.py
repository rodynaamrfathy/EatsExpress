#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from hashlib import md5


class Address(BaseModel, Base):
    """Representation of a user for EatExpress"""
    if models.storage_t == 'db':
        _tablename_ = 'Address'
        title = Column(String(20), nullable=True)
        address_line1 = Column(String(20), nullable=True)
        address_line2 = Column(String(20), nullable=True)
        city = Column(String(20), nullable=True)
        government = Column(String(20), nullable=True)
        postal_code = Column(String(20), nullable=True)
        country = Column(String(20), nullable=True)
        user_id = Column(String(60), nullable=False)
        user = relationship('User', back_populates='addresses')

    else:
        title = ""
        address_line1 = ""
        address_line2 = ""
        city = ""
        government = ""
        postal_code = ""
        country = "Egypt"
        user_id = ""

    def _init_(self, *args, **kwargs):
        """initializes user"""
        super()._init_(*args, **kwargs)

    def full_address(self):
            """Return a formatted full address."""
            parts = [self.address_line1, self.address_line2, self.city, self.government, self.postal_code, self.country]
            return ', '.join(part for part in parts if part)