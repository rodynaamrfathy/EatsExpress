<<<<<<< HEAD
# engine/db_storage.py

import models
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.User import User
from models.Order import Order
from models.Review import Review
from models.Restaurant import Restaurant
from os import getenv
import sqlalchemy
=======
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from os import getenv
>>>>>>> 865b44a (‘V2’)

classes = {"Restaurant": Restaurant  , "Review": Review, "Order": Order, "User": User}
class DBStorage:
    """Interacts with the SQL database"""

    __engine = None
    __session = None

    def __init__(self):
<<<<<<< HEAD
        EatExpress_MYSQL_USER = getenv("EatExpress_MYSQL_USER")
        EatExpress_MYSQL_PWD = getenv("EatExpress_MYSQL_PWD")
        EatExpress_MYSQL_DB = getenv("EatExpress_MYSQL_DB")
        EatExpress_MYSQL_HOST = getenv("EatExpress_MYSQL_HOST")
        EatExpress_ENV = getenv("EatExpress_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                    .format(EatExpress_MYSQL_USER, EatExpress_MYSQL_PWD, EatExpress_MYSQL_HOST, EatExpress_MYSQL_DB),
                                    pool_pre_ping=True)

        if EatExpress_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [ User, Order, Review, Restaurant]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)
    
=======
        """Instantiate a DBStorage object"""
        user = getenv('DB_USER')
        pwd = getenv('DB_PWD')
        host = getenv('DB_HOST')
        db = getenv('DB_NAME')
        db_type = getenv('DB_TYPE', 'sqlite')
        db_path = f"{db_type}:///../instance/site.db" if db_type == 'sqlite' else f"{db_type}://{user}:{pwd}@{host}/{db}"
        
        self.__engine = create_engine(db_path, pool_pre_ping=True)

    def all(self, cls=None):
        """Query on the current database session"""
        if cls is None:
            result = {}
            for cls_name in Base._decl_class_registry.values():
                if hasattr(cls_name, '__tablename__'):
                    result.update(self.__session.query(cls_name).all())
            return result
        else:
            return self.__session.query(cls).all()
>>>>>>> 865b44a (‘V2’)

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)


    def reload(self):
<<<<<<< HEAD
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()
=======
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
>>>>>>> 865b44a (‘V2’)

    @property
    def engine(self):
        """Get the engine"""
        return self.__engine

<<<<<<< HEAD

    
    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None
    
    
    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count


=======
    @property
    def session(self):
        """Get the session"""
        return self.__session
>>>>>>> 865b44a (‘V2’)
