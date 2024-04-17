#!/usr/bin/python3
"""This module defines a class to manage Database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session, scoped_session, relationship
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """database class"""

    __engine = None
    __session = None

    def __init__(self):
        """Initial method"""
        mysql_user = getenv("HBNB_MYSQL_USER")
        mysql_password = getenv("HBNB_MYSQL_PWD")
        mysql_host = getenv("HBNB_MYSQL_HOST")
        mysql_db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                mysql_user, mysql_password, mysql_host, mysql_db
            ),
            pool_pre_ping=True,
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """show all data"""
        if cls:
            objs = self.__session.query(cls).all()
        else:
            classes = [User, State, City, Amenity, Place, Review]
            objs = []
            for _class in classes:
                objs += self.__session.query(_class)
        new_dict = {}
        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """Add object in db"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()
