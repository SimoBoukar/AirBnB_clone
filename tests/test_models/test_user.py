#!/usr/bin/python3
"""
    Test for User
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests cases"""

    def setUp(self):
        """Set up test parameters."""
        self.user = User()

    def test_attributes(self):
        """Test the attributes are initialized correctly."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_inheritance(self):
        """Test the User class inherits from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == '__main__':
    unittest.main()
