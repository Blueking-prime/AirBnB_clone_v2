#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import stor_type
from models.city import City
from models.base_model import Base, BaseModel


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if stor_type == 'db':
        name = Column(String(128), nullable=False)

        cities = relationship("City", backref='state',
                              cascade="all, delete, delete-orphan")
    else:
        name = ''

    @property
    def cities(self):
        from models import storage
        dicts = storage.all(City)
        review_list = []
        for key in dicts.keys():
            if dicts[key]['state_id'] == self.id:
                review_list.append({key: dicts[key]})
        return review_list
