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
from models.Cart import Cart
from models.MenuItem import MenuItem
from os import getenv
import sqlalchemy

classes = {"User": User, "Order": Order, "Review": Review, "Restaurant": Restaurant, "Cart":Cart ,"MenuItem": MenuItem}
class DBStorage:
    """Interacts with the SQLAlchemy ORM"""
    __engine = None
    __session = None

    def _init_(self):
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
                key = "{}.{}".format(type(elem)._name_, elem.id)
                dic[key] = elem
        else:
            lista = [ User, Order, Review, Restaurant]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem)._name_, elem.id)
                    dic[key] = elem
        return (dic)
    

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
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """Close the current session"""
        self.__session.remove()


    
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