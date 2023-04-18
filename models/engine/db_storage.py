#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Defines db storage engine for hbnb clone"""

    __engine = None
    __session = None

    _classes = {
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):
        """Creates the db storage engine"""
        dbuser = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        dbhost = os.getenv("HBNB_MYSQL_HOST", default="localhost")
        dbname = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(dbuser,
                                                 passwd,
                                                 dbhost,
                                                 dbname),
            pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of the current database session by class name"""
        all_objs = {}
        for kcls in self._classes:
            if not cls or cls is self._classes[kcls]:
                for obj in self.__session.query(self._classes[kcls]).all():
                    key = "{}.{}".format(obj.__class__.__name, obj.id)
                    all_objs[key] = obj
        return all_objs

    def new(self, obj):
        """Add obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates the current database session from the engine"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)
