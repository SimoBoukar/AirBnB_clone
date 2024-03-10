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
        self.storage = FileStorage()

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

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()
