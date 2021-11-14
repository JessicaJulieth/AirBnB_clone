#!/usr/bin/python3
""" Unittest place"""
import unittest
from models.place import Place


obj_Place = Place()


class test_place(unittest.TestCase):
    """Test class for Place"""

    def test_obj(self):
        """Test if obj_Place is an instance of Place"""
        self.assertIsInstance(obj_Place, Place)

    def test_Place_name(self):
        """Checks if name is an atribute of Place"""
        self.assertTrue(hasattr(Place, "name"), True)

    def test_obj_name(self):
        """Checks if name is an atribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "name"), True)

    def test_id(self):
        """Test if id is an instance attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "id"), True)

    def test_created_at(self):
        """Test if created_at is an instance attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "created_at"), True)

    def test_updated_at(self):
        """Test if updated_at is an instance attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "updated_at"), True)

    def test_save(self):
        """Test if save is a method of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "save"), True)

    def test_to_dict(self):
        """Test if to_dict is a method of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "to_dict"), True)

    def test_city_id(self):
        """Test if city_id is an attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "city_id"), True)

    def test_name(self):
        """Test if name is an attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "name"), True)

    def test_description(self):
        """Test if description is an attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "description"), True)

    def test_number_rooms(self):
        """Test if number_rooms is an attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "number_rooms"), True)

    def test_number_bathrooms(self):
        """Test if number_bathrooms is an attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "number_bathrooms"), True)

    def test_max_guest(self):
        """Test if max_guest is an attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "max_guest"), True)

    def test_price_by_night(self):
        """Test if price_by_night is an attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "price_by_night"), True)

    def test_latitude(self):
        """Test if latitude is an attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "latitude"), True)

    def test_longitude(self):
        """Test if longitude is an attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "longitude"), True)

    def test_amenity_ids(self):
        """Test if amenity_ids is an attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Place, "amenity_ids"), True)
