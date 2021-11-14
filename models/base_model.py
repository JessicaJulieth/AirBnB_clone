#!/usr/bin/python3
""" base_Model Python Package"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """ Class BaseModel declaration

    Attributes
    id; UUID, universal unique identifier
    created_at; time of creation(datetime)
    updated_at; time of last update(datetime)

    Methods
    __str__; magic method to print
    save; update instance and updated_at value
    to_dict; method to dict
    """

    """__init__ Constructor"""
    def __init__(self, *args, **kwargs):
        """
        *args; argument string input
        **kwargs; argument key input
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    setattr(self, key, datetime.fromisoformat(value))

                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    """Methods"""
    def save(self):
        """ Updates updated_at value """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return new_dict, and update created_at and updated_at values"""
        Newdict = self.__dict__.copy()
        Newdict["__class__"] = self.__class__.__name__
        Newdict["created_at"] = Newdict["created_at"].isoformat()
        Newdict["updated_at"] = Newdict["updated_at"].isoformat()
        return Newdict

    """Magic methods"""
    def __str__(self):
        """ Str method to print """
        return("[{}] ({}) {}".
               format(self.__class__.__name__, self.id, self.__dict__))
