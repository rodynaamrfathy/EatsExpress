# models/base_model.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime

Base = declarative_base()

class BaseModel:
    """Base class for all models"""
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialize the base model"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        """Save the current instance"""
        from models import Session
        session = Session()
        session.add(self)
        session.commit()

    def delete(self):
        """Delete the current instance"""
        from models import Session
        session = Session()
        session.delete(self)
        session.commit()
