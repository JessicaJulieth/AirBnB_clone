#!/usr/bin/python3
""" Unittest FileStorage"""
import unittest
from models.engine.file_storage import FileStorage


obj_File = FileStorage()


class test_file_storage(unittest.TestCase):
    """Test class for FileStorage"""

    def test_obj_File(self):
        """Checks if obj_File is a FileStorage instance"""
        self.assertIsInstance(obj_File, FileStorage)

    def test_file_path(self):
        """Test if __file_path is an instance attribute of BaseModel"""
        self.assertFalse(hasattr(FileStorage, "__file_path"), False)

    def test_file_objects(self):
        """Test if __objects is an instance attribute of BaseModel"""
        self.assertFalse(hasattr(FileStorage, "__objects"), False)

    def test_all(self):
        """Test if all is a method of obj_File"""
        self.assertTrue(hasattr(obj_File, "all"), True)

    def test_new(self):
        """Test if new is a method of obj_File"""
        self.assertTrue(hasattr(obj_File, "new"), True)

    def test_save(self):
        """Test if save is a method of obj_File"""
        self.assertTrue(hasattr(obj_File, "save"), True)

    def test_reload(self):
        """Test if reload is a method of obj_File"""
        self.assertTrue(hasattr(obj_File, "reload"), True)
