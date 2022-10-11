#!/usr/bin/python3
""" State Module for HBNB project """
from email.policy import default
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
import os
from models.place import place_amenity
from models import stor_type
from models.base_model import Base, BaseModel


class Amenity(BaseModel, Base):
    '''Amneities eh'''
    __tablename__ = 'amenities'

    if stor_type == 'db':
        name = Column(String(128), nullable=False, default="")
        place_amenities  = relationship("place", secondary=place_amenity)
    else:
        name = ''
