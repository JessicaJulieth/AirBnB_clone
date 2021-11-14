#!/usr/bin/python3
""" Unittest City"""
import unittest
from models.city import City


obj_City = City()


class test_city(unittest.TestCase):
    """Test class for City"""

    def test_obj(self):
        """Test if obj_City is an instance of City"""
        self.assertIsInstance(obj_City, City)

    def test_obj_name(self):
        """Checks if name is an atribute of obj_City"""
        self.assertTrue(hasattr(obj_City, "name"), True)

    def test_name(self):
        """Checks if name is an atribute of City"""
        self.assertTrue(hasattr(City, "name"), True)

    def test_id(self):
        """Test if id is an instance attribute of obj_City"""
        self.assertTrue(hasattr(obj_City, "id"), True)

    def test_created_at(self):
        """Test if created_at is an instance attribute of obj_City"""
        self.assertTrue(hasattr(obj_City, "created_at"), True)

    def test_updated_at(self):
        """Test if updated_at is an instance attribute of obj_City"""
        self.assertTrue(hasattr(obj_City, "updated_at"), True)

    def test_save(self):
        """Test if save is a method of obj_City"""
        self.assertTrue(hasattr(obj_City, "save"), True)

    def test_to_dict(self):
        """Test if to_dict is a method of obj_City"""
        self.assertTrue(hasattr(obj_City, "to_dict"), True)
