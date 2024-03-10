#!/usr/bin/python3
"""
    Test for State
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests cases"""

    def setUp(self):
        """Set up test parameters."""
        self.state = State()

    def test_attributes(self):
        """Test the State attributes are initialized correctly."""
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        """Test the State class inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == '__main__':
    unittest.main()
