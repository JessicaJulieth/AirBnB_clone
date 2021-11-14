#!/usr/bin/python3
""" Unittest Amenity"""
import unittest
from models.amenity import Amenity


obj_Amenity = Amenity()


class test_amenity(unittest.TestCase):
    """Test for Amenity class"""

    def test_obj(self):
        """Test if obj_Amenity is an instance of Amenity"""
        self.assertIsInstance(obj_Amenity, Amenity)

    def test_obj_name(self):
        """Checks if name is an atribute of obj_Amenity"""
        self.assertTrue(hasattr(obj_Amenity, "name"), True)

    def test_Amenity_name(self):
        """Checks if name is an atribute of Amenity"""
        self.assertTrue(hasattr(Amenity, "name"), True)

    def test_id(self):
        """Test if id is an instance attribute of obj_Amenity"""
        self.assertTrue(hasattr(obj_Amenity, "id"), True)

    def test_created_at(self):
        """Test if created_at is an instance attribute of obj_Amenity"""
        self.assertTrue(hasattr(obj_Amenity, "created_at"), True)

    def test_updated_at(self):
        """Test if updated_at is an instance attribute of obj_Amenity"""
        self.assertTrue(hasattr(obj_Amenity, "updated_at"), True)

    def test_save(self):
        """Test if save is a method of obj_Amenity"""
        self.assertTrue(hasattr(obj_Amenity, "save"), True)

    def test_to_dict(self):
        """Test if to_dict is a method of obj_Amenity"""
        self.assertTrue(hasattr(obj_Amenity, "to_dict"), True)
