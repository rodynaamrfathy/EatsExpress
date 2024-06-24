#!/usr/bin/python3
"""Create a unique FileStorage or DBStorage instance for your application."""
import os
from models.base_model import Base
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Determine the storage type from the environment variable
storage_t = os.getenv('STORAGE_TYPE', 'db')

# Create the appropriate storage type
if storage_t == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

def init_db():
    """Initialize the database."""
    if storage_t == 'db':
        # Assuming models are imported correctly for metadata creation
        from models.User import User
        from models.Order import Order
        from models.Review import Review
        from models.Restaurant import Restaurant
        Base.metadata.create_all(storage.engine)

# Ensure that the DBStorage instance is initialized and tables are ready
storage.reload()
