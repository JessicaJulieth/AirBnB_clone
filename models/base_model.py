#!/usr/bin/python3
"""base_Model program"""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel that defines all common attributes/methods for other classes"""

    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        print("[{}] ({}) <{}>".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        if self.updated_at is not None:
            self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict.get("created_at", self.created_at.isoformat())
        new_dict.get("updated_at", self.updated_at.isoformat())
        new_dict["__class__"] = self.__class__.__name__
