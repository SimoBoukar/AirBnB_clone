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
            expected_output = "Creates a new instance of BaseModel,\n\
        saves it (to the JSON file) and prints the id"
            self.assertEqual(file_output.getvalue().strip(), expected_output)

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("? create")
            self.assertIsInstance(file_output.getvalue(), str)
            expected_output = "Creates a new instance of BaseModel,\n\
        saves it (to the JSON file) and prints the id"
            self.assertEqual(file_output.getvalue().strip(), expected_output)

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("? all")
            self.assertIsInstance(file_output.getvalue(), str)
            expected_output = "Prints all string representation of all \
instances\n        based or not on the class name."
            self.assertEqual(file_output.getvalue().strip(), expected_output)

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("help all")
            self.assertIsInstance(file_output.getvalue(), str)
            expected_output = "Prints all string representation of all \
instances\n        based or not on the class name."
            self.assertEqual(file_output.getvalue().strip(), expected_output)

        with patch('sys.stdout', new=StringIO()) as file_output:
            correct_msg = "Prints the string representation of an \
instancebased\n        based on the class name and id"
            HBNBCommand().onecmd("? show")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(),
                             correct_msg)

        with patch('sys.stdout', new=StringIO()) as file_output:
            correct_msg = "Prints the string representation of an \
instancebased\n        based on the class name and id"
            HBNBCommand().onecmd("help show")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(),
                             correct_msg)

        with patch('sys.stdout', new=StringIO()) as file_output:
            correct_msg = "Updates an instance based on the class name \
and id by adding\n        or updating attribute \
(save the change into the JSON file)."
            HBNBCommand().onecmd("? update")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(),
                             correct_msg)

        with patch('sys.stdout', new=StringIO()) as file_output:
            correct_msg = "Updates an instance based on the class name \
and id by adding\n        or updating attribute \
(save the change into the JSON file)."
            HBNBCommand().onecmd("help update")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(),
                             correct_msg)

        with patch('sys.stdout', new=StringIO()) as file_output:
            correct_msg = "Deletes an instance based on the class name \
and id\n        (save the change into the JSON file)"
            HBNBCommand().onecmd("? destroy")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(),
                             correct_msg)

        with patch('sys.stdout', new=StringIO()) as file_output:
            correct_msg = "Deletes an instance based on the class name \
and id\n        (save the change into the JSON file)"
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
            self.assertEqual(file_output.getvalue().strip(), "List available \
commands with \"help\" or detailed help with \"help cmd\".")

        with patch('sys.stdout', new=StringIO()) as file_output:
            HBNBCommand().onecmd("help help")
            self.assertIsInstance(file_output.getvalue(), str)
            self.assertEqual(file_output.getvalue().strip(), "List available \
commands with \"help\" or detailed help with \"help cmd\".")

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)


class TestBaseModel(unittest.TestCase):
    """Testing `Basemodel `commands."""
    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def testing_create_basemodel(self):
        """Test create basemodel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def testing_all_basemodel(self):
        """Test all basemodel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all BaseModel')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def test_show_basemodel(self):
        """Test show basemodel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            obj10 = BaseModel()
            obj10.eyes = "green"
            HBNBCommand().onecmd(f'show BaseModel {obj10.id}')
            res = f"[{type(obj10).__name__}] ({obj10.id}) {obj10.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def testing_update_basemodel(self):
        """Test update basemodel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            obj10 = BaseModel()
            obj10.name = "Cecilia"
            HBNBCommand().onecmd(f'update BaseModel {obj10.id} name "Ife"')
            self.assertEqual(obj10.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            obj10 = BaseModel()
            obj10.age = 75
            HBNBCommand().onecmd(f'update BaseModel {obj10.id} age 25')
            self.assertIn("age", obj10.__dict__.keys())
            self.assertEqual(obj10.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            obj10 = BaseModel()
            obj10.savings = 25.67
            HBNBCommand().onecmd(f'update BaseModel {obj10.id} savings 35.89')
            self.assertIn("savings", obj10.__dict__.keys())
            self.assertEqual(obj10.__dict__["savings"], 35.89)

        with patch('sys.stdout', new=StringIO()) as f:
            obj10 = BaseModel()
            obj10.age = 60
            cmmd = f'update BaseModel {obj10.id} age 10 color "green"'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", obj10.__dict__.keys())
            self.assertNotIn("color", obj10.__dict__.keys())
            self.assertEqual(obj10.__dict__["age"], 10)

    def testing_destroy_basemodel(self):
        """Test destroy basemodel object."""
        with patch('sys.stdout', new=StringIO()):
            obj10 = BaseModel()
            HBNBCommand().onecmd(f'destroy BaseModel {obj10.id}')
            self.assertNotIn("BaseModel.{}".format(
                obj10.id), storage.all().keys())

class TestBaseModelDotNotation(unittest.TestCase):
    """Testing `Basemodel `commands using dot notation."""

    def setUp(self):
        pass

    def testing_count_basemodel(self):
        """Test count basemodel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.count()'))
            counter = 0
            for i in storage.all().values():
                if type(i) == BaseModel:
                    counter += 1
            self.assertEqual(int(f.getvalue()), counter)

    def testing_all_basemodel(self):
        """Test all basemodel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def testing_show_basemodel(self):
        """Test show basemodel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            obj10 = BaseModel()
            obj10.eyes = "blue"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.show("{obj10.id}")'))
            res = f"[{type(obj10).__name__}] ({obj10.id}) {obj10.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def testing_update_basemodel(self):
        """Testing update basemodel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            obj10 = BaseModel()
            obj10.name = "Simo"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.update({obj10.id}, name, "Ife")'))
            self.assertEqual(obj10.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            obj10 = BaseModel()
            obj10.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.update({obj10.id}, age, 25)'))
            self.assertIn("age", obj10.__dict__.keys())
            self.assertEqual(obj10.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            obj10 = BaseModel()
            obj10.age = 60
            cmmd = f'BaseModel.update({obj10.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", obj10.__dict__.keys())
            self.assertNotIn("color", obj10.__dict__.keys())
            self.assertEqual(obj10.__dict__["age"], 10)

    def testing_update_basemodel_dict(self):
        """Test update basemodel object."""
        with patch('sys.stdout', new=StringIO()) as f:
            obj10 = BaseModel()
            obj10.age = 75
            cmmd = f'BaseModel.update({obj10.id}, {{"age": 25}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(obj10.__dict__["age"], 25)
            self.assertIsInstance(obj10.__dict__["age"], int)

    def testing_destroy_basemodel(self):
        """Test destroy basemodel object."""
        with patch('sys.stdout', new=StringIO()):
            obj10 = BaseModel()
            obj_id = obj10.id
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.destroy("{obj10.id}")'))
            self.assertNotIn(f"BaseModel.{obj_id}", storage.all().keys())
                
    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

class TestUser(unittest.TestCase):
    """Testing the `user` commands."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_user(self):
        """Test create user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_user(self):
        """Test all user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all User')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test show user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.eyes = "green"
            HBNBCommand().onecmd(f'show User {us.id}')
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test update user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.name = "Cecilia"
            HBNBCommand().onecmd(f'update User {us.id} name "Ife"')
            self.assertEqual(us.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            HBNBCommand().onecmd(f'update User {us.id} age 25')
            self.assertIn("age", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.savings = 25.67
            HBNBCommand().onecmd(f'update User {us.id} savings 35.89')
            self.assertIn("savings", us.__dict__.keys())
            self.assertEqual(us.__dict__["savings"], 35.89)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 60
            cmmd = f'update User {us.id} age 10 color green'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", us.__dict__.keys())
            self.assertNotIn("color", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 10)

    def test_destroy_user(self):
        """Test destroy user object.
        """
        with patch('sys.stdout', new=StringIO()):
            us = User()
            HBNBCommand().onecmd(f'destroy User {us.id}')
            self.assertNotIn("User.{}".format(
                us.id), storage.all().keys())

class TestUserDotNotation(unittest.TestCase):
    """Testing the `user` command's dot notation."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_count_user(self):
        """Test count user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == User:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_user(self):
        """Test all user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test show user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.show("{us.id}")'))
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test update user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.name = "Mostafa"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update("{us.id}", name, "Ife")'))
            self.assertEqual(us.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update("{us.id}", age, 25)'))
            self.assertIn("age", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 60
            cmmd = f'User.update("{us.id}", age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", us.__dict__.keys())
            self.assertNotIn("color", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 10)

    def test_update_user_dict(self):
        """Test update user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            cmmd = f'User.update("{us.id}", {{"age": 25, "color": "black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(us.__dict__["age"], 25)
            self.assertIsInstance(us.__dict__["age"], int)

    def test_destroy_user(self):
        """Test destroy user object.
        """
        with patch('sys.stdout', new=StringIO()):
            us = User()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.destroy("{us.id}")'))
            self.assertNotIn("User.{}".format(
                us.id), storage.all().keys())

class TestState(unittest.TestCase):
    """Testing the `state` commands."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_state(self):
        """Test create state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("State.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_state(self):
        """Test all state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all State')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

    def test_show_state(self):
        """Test show state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.eyes = "green"
            HBNBCommand().onecmd(f'show State {st.id}')
            res = f"[{type(st).__name__}] ({st.id}) {st.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_state(self):
        """Test update state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.name = "Cecilia"
            HBNBCommand().onecmd(f'update State {st.id} name "Ife"')
            self.assertEqual(st.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 75
            HBNBCommand().onecmd(f'update State {st.id} age 25')
            self.assertIn("age", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 60
            cmmd = f'update State {st.id} age 10 color green'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", st.__dict__.keys())
            self.assertNotIn("color", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 10)

    def test_destroy_state(self):
        """Test destroy state object.
        """
        with patch('sys.stdout', new=StringIO()):
            st = State()
            HBNBCommand().onecmd(f'destroy State {st.id}')
            self.assertNotIn("State.{}".format(
                st.id), storage.all().keys())

class TestStateDotNotation(unittest.TestCase):
    """Testing the `state` command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_count_state(self):
        """Test count state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == State:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_state(self):
        """Test all state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

    def test_show_state(self):
        """Test show state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.show("{st.id}")'))
            res = f"[{type(st).__name__}] ({st.id}) {st.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_state(self):
        """Test update state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update("{st.id}", name, "Ife")'))
            self.assertEqual(st.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update("{st.id}", age, 25)'))
            self.assertIn("age", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 60
            cmmd = f'State.update("{st.id}", age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", st.__dict__.keys())
            self.assertNotIn("color", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 10)

    def test_update_state_dict(self):
        """Test update state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 75
            cmmd = f'State.update("{st.id}", {{"age": 25, "color": "black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(st.__dict__["age"], 25)
            self.assertIsInstance(st.__dict__["age"], int)

    def test_destroy_state(self):
        """Test destroy state object.
        """
        with patch('sys.stdout', new=StringIO()):
            st = State()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.destroy("{st.id}")'))
            self.assertNotIn("State.{}".format(
                st.id), storage.all().keys())

class TestReview(unittest.TestCase):
    """Testing the `review` commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_review(self):
        """Test create review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Review')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Review.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_review(self):
        """Test all review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Review')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Review]')

    def test_show_review(self):
        """Test show review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.eyes = "green"
            HBNBCommand().onecmd(f'show Review {rv.id}')
            res = f"[{type(rv).__name__}] ({rv.id}) {rv.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_review(self):
        """Test update review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.name = "Cecilia"
            HBNBCommand().onecmd(f'update Review {rv.id} name "Ife"')
            self.assertEqual(rv.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 75
            HBNBCommand().onecmd(f'update Review {rv.id} age 25')
            self.assertIn("age", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 60
            cmmd = f'update Review {rv.id} age 10 color green)'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", rv.__dict__.keys())
            self.assertNotIn("color", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 10)

    def test_destroy_review(self):
        """Test destroy review object.
        """
        with patch('sys.stdout', new=StringIO()):
            rv = Review()
            HBNBCommand().onecmd(f'destroy Review {rv.id}')
            self.assertNotIn("Review.{}".format(
                rv.id), storage.all().keys())
