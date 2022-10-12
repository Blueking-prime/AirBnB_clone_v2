#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models import stor_type
from models.base_model import Base, BaseModel


class Amenity(BaseModel, Base):
    '''Amneities eh'''
    __tablename__ = 'amenities'

    if stor_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ''
