#!/usr/bin/python3
"""
    Test for Place
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Tests cases"""

    def setUp(self):
        """Set up test parameters."""
        self.place = Place()

    def test_attributes(self):
        """Test the attributes are initialized correctly."""
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.number_rooms, 0)
        self.assertAlmostEqual(self.place.longitude, 0.0)
        self.assertAlmostEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_inheritance(self):
        """Test the Place class inherits from BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == '__main__':
    unittest.main()
