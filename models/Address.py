#!/usr/bin/python3
""" holds class Address"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Address(BaseModel, Base):
    """Representation of an address for EatExpress"""
    if models.storage_t == 'db':
        __tablename__ = 'addresses'
        title = Column(String(128), nullable=False)
        address_line1 = Column(String(128), nullable=False)
        address_line2 = Column(String(128), nullable=True)
        city = Column(String(128), nullable=False)
        government = Column(String(128), nullable=False)
        postal_code = Column(String(128), nullable=False)
        country = Column(String(128), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
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

    def __init__(self, *args, **kwargs):
        """initializes address"""
        super().__init__(*args, **kwargs)

    def full_address(self):
        """Return a formatted full address."""
        parts = [self.address_line1, self.address_line2, self.city, self.government, self.postal_code, self.country]
        return ', '.join(part for part in parts if part)