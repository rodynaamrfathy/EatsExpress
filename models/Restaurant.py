#!/usr/bin/python3
""" Definition of the Restaurant model """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship

class Restaurant(BaseModel, Base):
    """ Representation of a Restaurant """
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    location = Column(String(256), nullable=True)
    cuisine_type = Column(String(128), nullable=True)
    average_cost = Column(Float, nullable=True)
    reviews = relationship("Review", backref="restaurant")

    def __init__(self, *args, **kwargs):
        """ Initializes the restaurant """
        super().__init__(*args, **kwargs)
