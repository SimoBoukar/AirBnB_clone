#!/usr/bin/python3
"""
    Test for Amenity
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Tests cases"""

    def setUp(self):
        """Set up test parameters."""
        self.amenity = Amenity()

    def test_attributes(self):
        """Test the attributes are initialized correctly."""
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """Test the Amenity class inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == '__main__':
    unittest.main()
