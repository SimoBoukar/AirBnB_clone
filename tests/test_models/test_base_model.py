#!/usr/bin/python3
"""
    Tests for BaseModel
"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Tests cases for BaseModel"""

    def setUp(self):
        """Set up test parameters."""
        self.model = BaseModel()

    def test_instance(self):
        """Test the instantiation of the BaseModel class."""
        self.assertIsInstance(self.model, BaseModel)

    def test_id_assigned(self):
        """Test if the id is assigned correctly."""
        self.assertTrue(hasattr(self.model, 'id'))

    def test_created_at_assigned(self):
        """Test if created_at is assigned correctly."""
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_assigned(self):
        """Test if updated_at is assigned correctly."""
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_method(self):
        """Test the save method updates updated_at."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_str_method(self):
        """Test the __str__ method returns the correct format."""
        self.assertEqual(
            str(self.model),
            f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        )

    def test_to_dict_method(self):
        """Test the to_dict method includes correct keys."""
        model_dict = self.model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertNotIn('_sa_instance_state', model_dict)

if __name__ == '__main__':
    unittest.main()
