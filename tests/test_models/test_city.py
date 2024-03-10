#!/usr/bin/python3
"""
    Test for City
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests cases"""

    def setUp(self):
        """Set up test parameters."""
        self.city = City()

    def test_attributes(self):
        """Test the attributes are initialized correctly."""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_inheritance(self):
        """Test the City class inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == '__main__':
    unittest.main()
