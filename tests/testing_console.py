#!/usr/bin/python3
""" Unittests cases for the console.py."""
from io import StringIO
import os
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """ Base class for testing Console."""

    def setUp(self):
        pass

    def testing_simple(self):
        """ Tests basic commands."""

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("quit")
            self.assertEqual(file_output.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(file_output.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("\n")
            self.assertEqual(file_output.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("?")
            self.assertIsInstance(file_output.getvalue(), str)

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("help")
            self.assertIsInstance(file_output.getvalue(), str)

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("help create")
            self.assertIsInstance(file_output.getvalue(), str)
            expected_output = "Creates a new instance of BaseModel,\n        saves it (to the JSON file) and prints the id"
            self.assertEqual(file_output.getvalue().strip(), expected_output)

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("? create")
            self.assertIsInstance(file_output.getvalue(), str)
            expected_output = "Creates a new instance of BaseModel,\n        saves it (to the JSON file) and prints the id"
            self.assertEqual(file_output.getvalue().strip(), expected_output)

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("? all")
            self.assertIsInstance(file_output.getvalue(), str)
            expected_output = "Prints all string representation of all instances\n        based or not on the class name."
            self.assertEqual(file_output.getvalue().strip(), expected_output)

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("help all")
            self.assertIsInstance(file_output.getvalue(), str)
            expected_output = "Prints all string representation of all instances\n        based or not on the class name."
            self.assertEqual(file_output.getvalue().strip(), expected_output)

        with patch('sys.stdout', new=StringIO()) as file_output:
            correct_msg = "Prints the string representation of an instancebased\n        based on the class name and id"
            HBNBCommand().onecmd("? show")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(),
                             correct_msg)

        with patch('sys.stdout', new=StringIO()) as file_output:
            correct_msg = "Prints the string representation of an instancebased\n        based on the class name and id"
            HBNBCommand().onecmd("help show")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(),
                             correct_msg)

        with patch('sys.stdout', new=StringIO()) as file_output:
            correct_msg = "Updates an instance based on the class name and id by adding\n        or updating attribute (save the change into the JSON file)."
            HBNBCommand().onecmd("? update")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(),
                             correct_msg)

        with patch('sys.stdout', new=StringIO()) as file_output:
            correct_msg = "Updates an instance based on the class name and id by adding\n        or updating attribute (save the change into the JSON file)."
            HBNBCommand().onecmd("help update")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(),
                             correct_msg)

        with patch('sys.stdout', new=StringIO()) as file_output:
            correct_msg = "Deletes an instance based on the class name and id\n        (save the change into the JSON file)"
            HBNBCommand().onecmd("? destroy")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(),
                             correct_msg)

        with patch('sys.stdout', new=StringIO()) as file_output:
            correct_msg = "Deletes an instance based on the class name and id\n        (save the change into the JSON file)"
            HBNBCommand().onecmd("help destroy")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(), correct_msg)

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("? quit")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(),
                             "Quit command to exit the program")

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("help quit")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(),
                             "Quit command to exit the program")

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("? help")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(), "List available commands with \"help\" or detailed help with \"help cmd\".")

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("help help")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(), "List available commands with \"help\" or detailed help with \"help cmd\".")

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)
