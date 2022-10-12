#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String,Integer, ForeignKey, Table
from models import stor_type
from models.base_model import Base, BaseModel
from models.place import place_amenity
from sqlalchemy.orm import relationship
import os



class Amenity(BaseModel, Base):
    '''Amneities eh'''
    __tablename__ = 'amenities'

    if stor_type == 'db':
        name = Column(String(128), nullable=False)
	place_amenities = relationship(
            "Place", secondary=place_amenity)
    else:
        name = ''
