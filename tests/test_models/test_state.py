#!/usr/bin/python3
"""State class unitTest"""
import unittest
from models.state import State


obj_State = State()


class test_state(unittest.TestCase):
    """Test class for State"""

    def test_obj(self):
        """Test if obj_State is an instance of State"""
        self.assertIsInstance(obj_State, State)

    def test_State_name(self):
        """Checks if name is an atribute of State"""
        self.assertTrue(hasattr(State, "name"), True)

    def test_obj_name(self):
        """Checks if name is an atribute of obj_State"""
        self.assertTrue(hasattr(obj_State, "name"), True)

    def test_id(self):
        """Test if id is an instance attribute of obj_State"""
        self.assertTrue(hasattr(obj_State, "id"), True)

    def test_created_at(self):
        """Test if created_at is an instance attribute of obj_State"""
        self.assertTrue(hasattr(obj_State, "created_at"), True)

    def test_updated_at(self):
        """Test if updated_at is an instance attribute of obj_State"""
        self.assertTrue(hasattr(obj_State, "updated_at"), True)

    def test_save(self):
        """Test if save is a method of obj_State"""
        self.assertTrue(hasattr(obj_State, "save"), True)

    def test_to_dict(self):
        """Test if to_dict is a method of obj_State"""
        self.assertTrue(hasattr(obj_State, "to_dict"), True)

    def test_name(self):
        """Test if name is an attribute of obj_State"""
        self.assertTrue(hasattr(obj_State, "name"), True)
