#!/usr/bin/python3

from models.state import State

dict1 = {"State.a397abec-507e-4f08-b9a0-2827318e773b": {"id": "a397abec-507e-4f08-b9a0-2827318e773b", "created_at": "2022-10-09T01:59:01.963132", "updated_at": "2022-10-09T01:59:01.963140", "name": "California", "__class__": "State"}, "Amenity.dca61c60-d8aa-412b-ba28-c2b990a3565b": {"id": "dca61c60-d8aa-412b-ba28-c2b990a3565b", "created_at": "2022-10-09T01:59:01.963175", "updated_at": "2022-10-09T01:59:01.963177", "name": "WiFi", "__class__": "Amenity"}, "State.6ea9a23d-22d6-42ce-b10e-ffd4a8c95695": {"id": "6ea9a23d-22d6-42ce-b10e-ffd4a8c95695", "created_at": "2022-10-09T01:59:01.963473", "updated_at": "2022-10-09T01:59:01.963477", "name": "Nevada", "__class__": "State"}}

def filter(cls=None):
    if cls is not None:
        filt = {}
        for key in dict1.keys():
            if dict1[key]['__class__'] == cls.__name__:
                print({key : dict1[key]})

filter(State)

