#!/usr/bin/python3
"""create a unique FileStorage or DBStorage instance for your application"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import Base

storage_t = os.getenv('STORAGE_TYPE', 'db')

if storage_t == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

def init_db():
    """Initialize the database"""
    if storage_t == 'db':
        import models.user
        import models.order
        import models.review
        Base.metadata.create_all(storage.engine)

storage.reload()
