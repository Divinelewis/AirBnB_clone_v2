#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all", backref="state")

    @property
    def cities(self):
        """Getter attribute - cities"""
        state_cities = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                state_cities.append(city)
        return state_cities
