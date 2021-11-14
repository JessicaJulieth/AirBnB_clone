#!/usr/bin/python3
""" Unittest __init__.py"""

import unittest
from models.__init__ import storage


class test__init__(unittest.TestCase):
    """Test class for __init__ file"""

    def test_storage(self):
        """function to check storage var exist"""
        self.assertTrue(storage), True
