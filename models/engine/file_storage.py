#!/usr/bin/python3
"""serializes instances to a JSON file
and deserializes JSON file to instances"""

from models.base_model import BaseModel
import json
from os import path


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
        New_dict = {}

        for key in self.__objects:
            New_dict[key] = self.__objects[key].to_dict()
        print(self.__objects)

        with open(self.__file_path, "w") as file:
            json.dump(New_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                json_obj = json.load(file)

            for key, value in json_obj.items():
                """created_key = json_obj[key]["__class__"]"""
                self.__objects[key] = BaseModel(**value)
