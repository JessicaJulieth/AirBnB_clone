#!/usr/bin/python3
"""serializes instances to a JSON file 
and deserializes JSON file to instances"""

import json
from os import path
from base_model import BaseModel

class FileStorage:
    """ Class FileStorage declaration

    Private class attributes:
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store 
    all objects by <class name>.id

    Methods
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file
    reload(self): deserializes the JSON file to __objects
    """

    # Private class attributes:
    __file_path = "file.json"
    __objects = {}
    
    # Public instance methods:
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key 
        <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        for key in self.__objects:
            with open(self.__file_path, "w") as file:
                json.dumps(self.__objects, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if path.isfile(self.__file_path):
            with open(self.__file_path, "w") as file:
                self.__objects = json.load(self.__objects)
