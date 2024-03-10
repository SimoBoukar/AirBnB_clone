#!/usr/bin/python3
"""
    Test for Review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Tests cases"""

    def setUp(self):
        """Set up test parameters."""
        self.review = Review()

    def test_attributes(self):
        """Test the attributes are initialized correctly."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        """Test the Review class inherits from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == '__main__':
    unittest.main()
