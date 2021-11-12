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

    # __init__ Constructor
    def __init__(self, *args, **kwargs):
        """
        *args; argument string input
        **kwargs; argument key input
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    kwargs[key] = datetime.strptime
                    (key, "%Y-%m-%dT%H:%M:%S.%f")

                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    # Methods
    def save(self):
        """ Updates updated_at value """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return new_dict, and update created_at and updated_at values """
        name = self.__class__.__name__
        New_dict = self.__dict__.copy()
        New_dict.update(__class__=name, created_at=self.created_at.isoformat())
        New_dict.update(updated_at=self.updated_at.isoformat())

        return New_dict

    # Magic methods
    def __str__(self):
        """ Str method to print """
        return("[{}] ({}) {}".format
        (self.__class__.__name__, self.id, self.__dict__))
