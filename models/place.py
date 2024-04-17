#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60),ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60),ForeignKey('users.id'), nullable=False)
    name =  Column(String(128), nullable=False)
    description =  Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False,default=0)
    number_bathrooms = Column(Integer, nullable=False,default=0)
    max_guest = Column(Integer, nullable=False,default=0)
    price_by_night = Column(Integer, nullable=False,default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="Place")

    def reviews(self):
        """getter attribute reviews that returns the list of Review"""
        from models.review import Review
        review_list = []
        all_reviews = models.storage.all(Review)
        for review in all_reviews.values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list
