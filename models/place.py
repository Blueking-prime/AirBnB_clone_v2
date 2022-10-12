#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from models import stor_type
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base, BaseModel
import os
import models

if stor_type == 'db':
    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            primary_key=True),
        Column(
            'amenity_id',
            String(60),
            ForeignKey('amenities.id'),
            primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if stor_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []

        reviews = relationship(
            "Review",
            back_populates='place',
            cascade="all, delete, delete-orphan")
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            backref='place_amenities',
            viewonly=False)
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
        '''returns the list of Review instances
        with place_id equals to the current Place.id'''
        from models import storage
        dicts = storage.all(Review)
        review_list = []
        for key in dicts.keys():
            if dicts[key]['place_id'] == self.id:
                review_list.append(dicts[key])
        return review_list

    @property
    def amenities(self):
        '''returns the list of Amenity instances
        based on the attribute amenity_ids'''
        from models import storage
        dicts = storage.all(Amenity)
        amenities_list = []
        for key in dicts.keys():
            if dicts[key]['place_id'] in self.amenity_ids:
                amenities_list.append(dicts[key])
        return amenities_list

    @amenities.setter
    def amenities(self, obj):
        '''handles append method
        for adding an Amenity.id to the attribute amenity_ids'''
        if obj is not None and isinstance(obj, Amenity):
            if obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
