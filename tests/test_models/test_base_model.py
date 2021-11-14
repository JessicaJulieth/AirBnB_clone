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
        """Test if save is a method of BaseModel"""
        self.assertTrue(hasattr(obj_Base, "save"), True)

    def test_to_dict(self):
        """Test if to_dict is a method of BaseModel"""
        self.assertTrue(hasattr(obj_Base, "to_dict"), True)
