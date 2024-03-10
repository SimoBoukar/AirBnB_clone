#!/usr/bin/python3
"""
    Tests for FileStorage
"""
import unittest
import json
from models.engine.file_storage import FileStorage, BaseModel, User, State
from models.engine.file_storage import City, Amenity, Place, Review
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests cases for FileStorage"""

    def setUp(self):
        """Prepare the test fixture before each test method."""
        self.test_storage = FileStorage()

    def test_all_returns_dict(self):
        """Test if 'all' method returns a dictionary."""
        self.assertIsInstance(self.test_storage.all(), dict)

    def test_new_method(self):
        """Test the 'new' method for adding objects."""
        obj = BaseModel()
        self.test_storage.new(obj)
        self.assertIn(obj, self.test_storage.all().values())

    def test_save_method(self):
        """Test the 'save' method."""
        obj = BaseModel()
        self.test_storage.new(obj)
        obj_id = obj.id
        k = "{}.{}".format(obj.__class__.__name__, obj_id)
        self.test_storage.save()
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
        self.assertIn(k, data.keys())

    def test_reload_method(self):
        """Test the 'reload' method."""
        self.test_storage.reload()
        self.assertTrue(hasattr(self.test_storage, '_FileStorage__objects'))
        self.assertIsInstance(self.test_storage._FileStorage__objects, dict)


if __name__ == '__main__':
    unittest.main()
