#!/usr/bin/python3
""" base_Model Python module"""

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
            for key in kwargs:
                if key is not __class__:
                    for value in kwargs.items():
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    # Methods
    def save(self):
        """ Updates updated_at value """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return new_dict, and update created_at and updated_at values """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict.get("created_at", self.created_at.isoformat())
        new_dict.get("updated_at", self.updated_at.isoformat())
        return new_dict

    # Magic methods
    def __str__(self):
        """ Str method to print """
        print("[{}] ({}) {}"
        .format(self.__class__.__name__, self.id, self.__dict__))
