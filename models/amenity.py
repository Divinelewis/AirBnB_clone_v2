#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String

from models.base_model import Base, BaseModel


class Amenity(BaseModel, Base):
    """Defines an amenity"""

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
