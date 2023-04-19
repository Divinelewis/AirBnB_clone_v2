#!/usr/bin/python3
""" Place Module for HBNB project """

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
import os
from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.review import Review
import models
from sqlalchemy.sql.schema import Table

if storage_type == 'db':
    place_amenities = Table("place_amenity", Base.metadata,
                        Column("place_id", String(60),
                               ForeignKey("places.id"),
                               primary_key=True,
                               nullable=False),
                        Column("amenity_id", String(60),
                               ForeignKey("amenity.id"),
                               primary_key=True,
                               nullable=False),
                        )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            reviews = relationship("Review", cascade="all, delete, delete-orphan", backref="place")
            amenities = relationship("Amenity", secondary=place_amenity, backref='place_amenities' viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Returns a list of Review instances with self.id as place_id"""
            place_reviews = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    place_reviews.append(review)
            return place_reviews

        @property
        def amenities(self):
            """Amenities getter"""
            self_amenities = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.place_id == self.id:
                    self_amenities.append(amenity)
            return self_amenities

        @amenities.setter
        def amenities(self, amenity):
            """Amenities setter"""
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity)
