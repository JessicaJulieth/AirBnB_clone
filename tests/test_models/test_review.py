#!/usr/bin/python3
""" Unittest Review"""
import unittest
from models.review import Review


obj_Review = Review()


class test_review(unittest.TestCase):
    """Test class Review"""

    def test_obj(self):
        """Test if obj_Review is an instance of Review"""
        self.assertIsInstance(obj_Review, Review)

    def test_id(self):
        """Test if id is an instance attribute of obj_Review"""
        self.assertTrue(hasattr(obj_Review, "id"), True)

    def test_created_at(self):
        """Test if created_at is an instance attribute of obj_Review"""
        self.assertTrue(hasattr(obj_Review, "created_at"), True)

    def test_updated_at(self):
        """Test if updated_at is an instance attribute of obj_Review"""
        self.assertTrue(hasattr(obj_Review, "updated_at"), True)

    def test_save(self):
        """Test if save is a method of obj_Review"""
        self.assertTrue(hasattr(obj_Review, "save"), True)

    def test_to_dict(self):
        """Test if to_dict is a method of obj_Review"""
        self.assertTrue(hasattr(obj_Review, "to_dict"), True)

    def test_place_id(self):
        """Test if place_id is an attribute of obj_Review"""
        self.assertTrue(hasattr(obj_Review, "place_id"), True)

    def test_user_id(self):
        """Test if user_id is an attribute of obj_Place"""
        self.assertTrue(hasattr(obj_Review, "user_id"), True)

    def test_text(self):
        """Test if text is an attribute of obj_Review"""
        self.assertTrue(hasattr(obj_Review, "text"), True)
