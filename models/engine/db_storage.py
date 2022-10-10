#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

usr = getenv('HBNB_MYSQL_USER')
pwd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
env = getenv('HBNB_ENV')

class DBStorage:
    """This class manages storage of hbnb models in MySQL"""
    __engine = None
    Sess = sessionmaker()
    __session = Sess()
    # __session = None

    def __init__(self):
        url_str = f'mysql+mysqldb://{usr}:{pwd}@{host}/{db}'
        self.__engine = create_engine(url_str, pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all()
        Session = sessionmaker(bind=self.__engine)

    def all(self, cls=None):
        '''query on the current database session
         all objects depending of the class name'''
        if cls is not None:
            filt_obj_dict = {}
            for key in self.__session.query(cls):
                filt_obj_dict.update(key)
            return filt_obj_dict
        obj_dict = {}
        objects = self.__session.query(User, State, City, Amenity, Place, Review)
        for item in objects:
            obj_dict.update(item)

    def new(self, obj):
        '''add the object to the current database session'''
        self.__session.add(obj)

    def save(self):
        '''commit all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete from the current database session obj if not None'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''reloads all database tables and reinitializes engine'''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
