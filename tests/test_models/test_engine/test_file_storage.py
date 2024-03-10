#!/usr/bin/python3
"""
    Tests for FileStorage
"""
import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests cases for FileStorage"""
    def setUp(self):
        """Prepare the test fixture before each test method."""
        self.storage = FileStorage()
        setattr(FileStorage, "_FileStorage__objects", {})

    def tearDown(self):
        """Clean storage file"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all_returns_dict(self):
        """Test if 'all' method returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_method(self):
        """Test the 'new' method for adding objects."""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(obj, self.storage.all().values())

    def test_save_method(self):
        """Test the 'save' method."""
        obj = BaseModel()
        self.storage.new(obj)
        obj_id = obj.id
        k = "{}.{}".format(obj.__class__.__name__, obj_id)
        self.storage.save()
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
        self.assertIn(k, data.keys())

    def test_reload_method(self):
        """Test the 'reload' method."""
        self.storage.reload()
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_new(self):
        """Test new method"""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn("BaseModel." + obj.id, all_objs)

    def test_reload_empty_file(self):
        """Test to reload an empty file"""
        open(FileStorage._FileStorage__file_path, "w").close()
        test_storage = FileStorage()
        test_storage.reload()
        all_objs = test_storage.all()
        self.assertEqual(len(all_objs), 0)


if __name__ == '__main__':
    unittest.main()
