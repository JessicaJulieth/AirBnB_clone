#!/usr/bin/python3
""" Unittest BaseModel"""
import unittest
from models.base_model import BaseModel


obj_Base = BaseModel()


class test_base_model(unittest.TestCase):
    """Test the obj_Base object attributes"""

    def test_obj_Base(self):
        """Checks if obj_Base is a BaseModel instance"""
        self.assertIsInstance(obj_Base, BaseModel)

    def test_id(self):
        """Test if id is an instance attribute of BaseModel"""
        self.assertTrue(hasattr(obj_Base, "id"), True)

    def test_created_at(self):
        """Test if created_at is an instance attribute of BaseModel"""
        self.assertTrue(hasattr(obj_Base, "created_at"), True)

    def test_updated_at(self):
        """Test if updated_at is an instance attribute of BaseModel"""
        self.assertTrue(hasattr(obj_Base, "updated_at"), True)

    def test_save(self):
        """Test if the date is updating"""
        now = obj_Base.updated_at
        obj_Base.save()
        now2 = obj_Base.updated_at
        self.assertNotEqual(now, now2)
        
    def test_save_2(self):
        """Test if save is a method of BaseModel""" 
        self.assertTrue(hasattr(BaseModel, "save"), True)

    def test_to_dict(self):
        """Test if to_dict is a dict"""
        new_dict = obj_Base.to_dict()
        self.assertIsInstance(new_dict, dict)
        
    def test_to_dict_2(self):
        """Test if to_dict is a method of BaseModel"""
        self.assertTrue(hasattr(BaseModel, "to_dict"), True)

    def test_to_str(self):
        """Test if __str__ is a method of BaseModel"""
        self.assertTrue(hasattr(BaseModel, "__str__"), True)
