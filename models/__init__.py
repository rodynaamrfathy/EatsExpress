#!/usr/bin/python3
<<<<<<< HEAD
"""create a unique FileStorage instance for your application"""
from os import getenv
=======
"""Create a unique FileStorage or DBStorage instance for your application."""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
>>>>>>> 865b44a (‘V2’)



storage_t = getenv("EatExpress_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
<<<<<<< HEAD
storage.reload()
=======

# Ensure that the DBStorage instance is initialized and tables are ready
storage.reload()

def init_db():
    """Initialize the database."""
    if storage_t == 'db':
        from models.base_model import Base
        from models.User import User
        from models.Order import Order
        from models.Review import Review
        from models.Restaurant import Restaurant
        from models.MenuItem import MenuItem
        from models.Cart import Cart
        Base.metadata.create_all(storage.engine)
>>>>>>> 865b44a (‘V2’)
