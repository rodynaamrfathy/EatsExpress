# models/__init__.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

storage_t = os.getenv('STORAGE_TYPE', 'db')
if storage_t == 'db':
    engine = create_engine('sqlite:///eatexpress.db')
    Session = scoped_session(sessionmaker(bind=engine))
else:
    # Code for file storage or other types of storage
    Session = None

def init_db():
    """Initialize the database"""
    import models.base_model
    import models.user
    import models.order
    import models.review
    Base.metadata.create_all(engine)
