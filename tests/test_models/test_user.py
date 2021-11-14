#!/usr/bin/python3
""" Unittest User"""
import unittest
from models.user import User


obj_User = User()


class test_user(unittest.TestCase):
    """Test class for User"""

    def test_obj(self):
        """Test if obj_Place is an instance of Place"""
        self.assertIsInstance(obj_User, User)

    def test_id(self):
        """Test if id is an instance attribute of obj_User"""
        self.assertTrue(hasattr(obj_User, "id"), True)

    def test_created_at(self):
        """Test if created_at is an instance attribute of obj_User"""
        self.assertTrue(hasattr(obj_User, "created_at"), True)

    def test_updated_at(self):
        """Test if updated_at is an instance attribute of obj_User"""
        self.assertTrue(hasattr(obj_User, "updated_at"), True)

    def test_save(self):
        """Test if save is a method of obj_User"""
        self.assertTrue(hasattr(obj_User, "save"), True)

    def test_to_dict(self):
        """Test if to_dict is a method of obj_User"""
        self.assertTrue(hasattr(obj_User, "to_dict"), True)

    def test_email(self):
        """Test if email is an attribute of obj_User"""
        self.assertTrue(hasattr(obj_User, "email"), True)

    def test_password(self):
        """Test if password is an attribute of obj_User"""
        self.assertTrue(hasattr(obj_User, "password"), True)

    def test_first_name(self):
        """Test if first_name is an attribute of obj_User"""
        self.assertTrue(hasattr(obj_User, "first_name"), True)

    def test_last_name(self):
        """Test if last_name is an attribute of obj_User"""
        self.assertTrue(hasattr(obj_User, "last_name"), True)
