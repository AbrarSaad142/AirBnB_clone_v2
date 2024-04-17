#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
class State(BaseModel,Base):
    """ State class
    Attribute:
        name: input name
    """
    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        name = ""

        @property
        def cities(self):
            """ Return a list of city"""
            the_cities = []
            for c in models.storage.all(City).values():
                if c.state_id == self.id:
                    the_cities.append(c)
            return the_cities
