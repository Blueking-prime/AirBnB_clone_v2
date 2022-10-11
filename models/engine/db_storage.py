#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models import usr, pwd, db, host, env
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in MySQL"""
    __engine = None
    __session = None

    def __init__(self):
        url_str = f'mysql+mysqldb://{usr}:{pwd}@{host}/{db}'
        self.__engine = create_engine(url_str, pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''query on the current database session
         all objects depending of the class name'''
        if cls is not None:
            filt_obj_dict = {}
            for obj in self.__session.query(cls).all():
                key = obj.__class__.__name__ + '.' + obj.id
                filt_obj_dict.update({key: obj})
            return filt_obj_dict
        obj_dict = {}
        for clss in [User, State, City, Amenity, Place, Review]:
            objects = self.__session.query(clss).all()
            for obj in objects:
                key = obj.__class__.__name__ + '.' + obj.id
                obj_dict.update({key: obj})
        return obj_dict

    def new(self, obj):
        '''add the object to the current database session'''
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        '''commit all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete from the current database session obj if not None'''
        if obj is not None:
            self.__session.query(type(obj)).\
                filter(type(obj).id == obj.id).\
                delete()

    def reload(self):
        '''reloads all database tables and reinitializes engine'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
