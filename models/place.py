#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base, BaseModel


place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

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

    reviews = relationship("Review", back_populates='place',
                cascade="all, delete, delete-orphan")

    user = relationship("User", back_populates='places')
    cities = relationship("City", back_populates='places')
    amenities = relationship("Amenity", secondary=place_amenity, back_populates='place_amenities', viewonly=False)

    @property
    def reviews(self):
        from models import storage
        dicts = storage.all(Review)
        review_list = []
        for key in dicts.keys():
            if dicts[key]['place_id'] == self.id:
                review_list.append({key : dicts[key]})
        return review_list

    @property
    def amenities(self):
        from models import storage
        dicts = storage.all(Amenity)
        review_list = []
        for key in dicts.keys():
            if dicts[key]['place_id'] == self.id:
                review_list.append({key : dicts[key]})
        return review_list
