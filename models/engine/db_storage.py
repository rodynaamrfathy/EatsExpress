# engine/db_storage.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

class DBStorage:
    """Interacts with the SQLAlchemy ORM"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST')
        db = os.getenv('DB_NAME')
        db_type = os.getenv('DB_TYPE', 'sqlite')

        if db_type == 'mysql':
            self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db}')
        else:
            self.__engine = create_engine('sqlite:///eatexpress.db')

    def all(self, cls=None):
        """Query on the current database session"""
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = []
            for class_name in Base._decl_class_registry.values():
                if isinstance(class_name, type):
                    objs.extend(self.__session.query(class_name).all())
        return {obj.__class__.__name__ + '.' + str(obj.id): obj for obj in objs}

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload all tables"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the current session"""
        self.__session.remove()
