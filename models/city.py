#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models import stor_type
from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    if stor_type == 'db':
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)

        places = relationship("Place", backref='cities',
                              cascade="all, delete, delete-orphan")
    else:
        state_id = ''
        name = ''
