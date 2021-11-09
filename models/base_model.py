#!/usr/bin/python3
""" base_Model program """

import uuid
from datetime import datetime


class BaseModel:
    """ Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """ Class BaseModel atributte constructor """
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Str method to print """
        print("[{}] ({}) {}"
        .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Updates updated_at value """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return new_dict, and update created_at and updated_at values """
        new_dict = self.__dict__.copy()
        new_dict.get("created_at", self.created_at.isoformat())
        new_dict.get("updated_at", self.updated_at.isoformat())
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
