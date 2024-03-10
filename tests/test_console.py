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
                if type(i) is BaseModel:
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
            user = User()
            user.eyes = "green"
            HBNBCommand().onecmd(f'show User {user.id}')
            res = f"[{type(user).__name__}] ({user.id}) {user.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test update user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.name = "MOSTAFAAAAAAA"
            HBNBCommand().onecmd(f'update User {user.id} name "Ife"')
            self.assertEqual(user.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.age = 75
            HBNBCommand().onecmd(f'update User {user.id} age 25')
            self.assertIn("age", user.__dict__.keys())
            self.assertEqual(user.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.savings = 25.67
            HBNBCommand().onecmd(f'update User {user.id} savings 35.89')
            self.assertIn("savings", user.__dict__.keys())
            self.assertEqual(user.__dict__["savings"], 35.89)

        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.age = 60
            cmmd = f'update User {user.id} age 10 color green'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", user.__dict__.keys())
            self.assertNotIn("color", user.__dict__.keys())
            self.assertEqual(user.__dict__["age"], 10)

    def test_destroy_user(self):
        """Test destroy user object."""
        with patch('sys.stdout', new=StringIO()):
            user = User()
            HBNBCommand().onecmd(f'destroy User {user.id}')
            self.assertNotIn("User.{}".format(
                user.id), storage.all().keys())


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
        """Test count user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.count()'))
            counter = 0
            for i in storage.all().values():
                if type(i) is User:
                    counter += 1
            self.assertEqual(int(f.getvalue()), counter)

    def test_all_user(self):
        """Test all user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test show user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.show("{user.id}")'))
            res = f"[{type(user).__name__}] ({user.id}) {user.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test update user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.name = "Mostafa"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update("{user.id}", name, "Ife")'))
            self.assertEqual(user.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update("{user.id}", age, 25)'))
            self.assertIn("age", user.__dict__.keys())
            self.assertEqual(user.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.age = 60
            cmmd = f'User.update("{user.id}", age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", user.__dict__.keys())
            self.assertNotIn("color", user.__dict__.keys())
            self.assertEqual(user.__dict__["age"], 10)

    def test_update_user_dict(self):
        """Test update user object."""
        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.age = 75
            cmmd = f'User.update("{user.id}", {{"age": 25, "color": "black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(user.__dict__["age"], 25)
            self.assertIsInstance(user.__dict__["age"], int)

    def test_destroy_user(self):
        """Test destroy user object."""
        with patch('sys.stdout', new=StringIO()):
            user = User()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.destroy("{user.id}")'))
            self.assertNotIn("User.{}".format(
                user.id), storage.all().keys())


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
        """Test create state object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("State.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_state(self):
        """Test all state object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all State')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

    def test_show_state(self):
        """Test show state object."""
        with patch('sys.stdout', new=StringIO()) as f:
            sta = State()
            sta.eyes = "RED"
            HBNBCommand().onecmd(f'show State {sta.id}')
            res = f"[{type(sta).__name__}] ({sta.id}) {sta.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_state(self):
        """Test update state object."""
        with patch('sys.stdout', new=StringIO()) as f:
            sta = State()
            sta.name = "MOSTAFAA"
            HBNBCommand().onecmd(f'update State {sta.id} name "Ife"')
            self.assertEqual(sta.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            sta = State()
            sta.age = 75
            HBNBCommand().onecmd(f'update State {sta.id} age 25')
            self.assertIn("age", sta.__dict__.keys())
            self.assertEqual(sta.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            sta = State()
            sta.age = 60
            cmmd = f'update State {sta.id} age 10 color green'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", sta.__dict__.keys())
            self.assertNotIn("color", sta.__dict__.keys())
            self.assertEqual(sta.__dict__["age"], 10)

    def test_destroy_state(self):
        """Test destroy state object."""
        with patch('sys.stdout', new=StringIO()):
            sta = State()
            HBNBCommand().onecmd(f'destroy State {sta.id}')
            self.assertNotIn("State.{}".format(
                sta.id), storage.all().keys())


class TestStateDotNotation(unittest.TestCase):
    """Testing the `state` command's dot notation."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_count_state(self):
        """Test count state object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.count()'))
            counter = 0
            for i in storage.all().values():
                if type(i) is State:
                    counter += 1
            self.assertEqual(int(f.getvalue()), counter)

    def test_all_state(self):
        """Test all state object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

    def test_show_state(self):
        """Test show state object."""
        with patch('sys.stdout', new=StringIO()) as f:
            sta = State()
            sta.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.show("{sta.id}")'))
            res = f"[{type(sta).__name__}] ({sta.id}) {sta.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_state(self):
        """Test update state object."""
        with patch('sys.stdout', new=StringIO()) as f:
            sta = State()
            sta.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update("{sta.id}", name, "Ife")'))
            self.assertEqual(sta.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            sta = State()
            sta.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update("{sta.id}", age, 25)'))
            self.assertIn("age", sta.__dict__.keys())
            self.assertEqual(sta.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            sta = State()
            sta.age = 60
            cmmd = f'State.update("{sta.id}", age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", sta.__dict__.keys())
            self.assertNotIn("color", sta.__dict__.keys())
            self.assertEqual(sta.__dict__["age"], 10)

    def test_update_state_dict(self):
        """Test update state object."""
        with patch('sys.stdout', new=StringIO()) as f:
            sta = State()
            sta.age = 75
            cmmd = f'State.update("{sta.id}", {{"age": 25, "color": "black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(sta.__dict__["age"], 25)
            self.assertIsInstance(sta.__dict__["age"], int)

    def test_destroy_state(self):
        """Test destroy state object."""
        with patch('sys.stdout', new=StringIO()):
            sta = State()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.destroy("{sta.id}")'))
            self.assertNotIn("State.{}".format(
                sta.id), storage.all().keys())


class TestReview(unittest.TestCase):
    """Testing the `review` commands."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_review(self):
        """Test create review object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Review')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Review.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_review(self):
        """Test all review object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Review')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Review]')

    def test_show_review(self):
        """Test show review object."""
        with patch('sys.stdout', new=StringIO()) as f:
            rva = Review()
            rva.eyes = "green"
            HBNBCommand().onecmd(f'show Review {rva.id}')
            res = f"[{type(rva).__name__}] ({rva.id}) {rva.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_review(self):
        """Test update review object."""
        with patch('sys.stdout', new=StringIO()) as f:
            rva = Review()
            rva.name = "RAFMOOOOOOOOOOOOOOOOOOOOOOS"
            HBNBCommand().onecmd(f'update Review {rva.id} name "Ife"')
            self.assertEqual(rva.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            rva = Review()
            rva.age = 75
            HBNBCommand().onecmd(f'update Review {rva.id} age 25')
            self.assertIn("age", rva.__dict__.keys())
            self.assertEqual(rva.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            rva = Review()
            rva.age = 60
            cmmd = f'update Review {rva.id} age 10 color green)'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", rva.__dict__.keys())
            self.assertNotIn("color", rva.__dict__.keys())
            self.assertEqual(rva.__dict__["age"], 10)

    def test_destroy_review(self):
        """Test destroy review object."""
        with patch('sys.stdout', new=StringIO()):
            rva = Review()
            HBNBCommand().onecmd(f'destroy Review {rva.id}')
            self.assertNotIn("Review.{}".format(
                rva.id), storage.all().keys())


class TestReviewDotNotation(unittest.TestCase):
    """Testing the `review` command's dot notation."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_count_review(self):
        """Test count review object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.count()'))
            counter = 0
            for i in storage.all().values():
                if type(i) is Review:
                    counter += 1
            self.assertEqual(int(f.getvalue()), counter)

    def test_all_review(self):
        """Test all review object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Review]')

    def test_show_review(self):
        """Test show review object."""
        with patch('sys.stdout', new=StringIO()) as f:
            rva = Review()
            rva.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.show("{rva.id}")'))
            res = f"[{type(rva).__name__}] ({rva.id}) {rva.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_review(self):
        """Test update review object."""
        with patch('sys.stdout', new=StringIO()) as f:
            rva = Review()
            rva.name = "RAFMOS"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update("{rva.id}", name, "Ife")'))
            self.assertEqual(rva.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            rva = Review()
            rva.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update("{rva.id}", age, 25)'))
            self.assertIn("age", rva.__dict__.keys())
            self.assertEqual(rva.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            rva = Review()
            rva.age = 60
            cmmd = f'Review.update("{rva.id}", age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", rva.__dict__.keys())
            self.assertNotIn("color", rva.__dict__.keys())
            self.assertEqual(rva.__dict__["age"], 10)

    def test_update_review_dict(self):
        """Test update review object."""
        with patch('sys.stdout', new=StringIO()) as f:
            v = Review()
            v.age = 75
            cmmd = f'Review.update("{v.id}", {{"age": 25, "color": "black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(v.__dict__["age"], 25)
            self.assertIsInstance(v.__dict__["age"], int)

    def test_destroy_review(self):
        """Test destroy review object."""
        with patch('sys.stdout', new=StringIO()):
            rva = Review()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.destroy("{rva.id}")'))
            self.assertNotIn("Review.{}".format(
                rva.id), storage.all().keys())


class TestPlace(unittest.TestCase):
    """Testing the `place` commands."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_place(self):
        """Test create place object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Place.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_place(self):
        """Test all place object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Place')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Place]')

    def test_show_place(self):
        """Test show place object."""
        with patch('sys.stdout', new=StringIO()) as f:
            pla = Place()
            pla.eyes = "green"
            HBNBCommand().onecmd(f'show Place {pla.id}')
            res = f"[{type(pla).__name__}] ({pla.id}) {pla.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_place(self):
        """Test update place object."""
        with patch('sys.stdout', new=StringIO()) as f:
            pla = Place()
            pla.name = "MOSTAFA"
            HBNBCommand().onecmd(f'update Place {pla.id} name "Ife"')
            self.assertEqual(pla.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            pla = Place()
            pla.age = 75
            HBNBCommand().onecmd(f'update Place {pla.id} age 25')
            self.assertIn("age", pla.__dict__.keys())
            self.assertEqual(pla.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            pla = Place()
            pla.age = 60
            cmmd = f'update Place {pla.id} age 10 color green'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", pla.__dict__.keys())
            self.assertNotIn("color", pla.__dict__.keys())
            self.assertEqual(pla.__dict__["age"], 10)

    def test_destroy_place(self):
        """Test destroy place object."""
        with patch('sys.stdout', new=StringIO()):
            pla = Place()
            HBNBCommand().onecmd(f'destroy Place {pla.id}')
            self.assertNotIn("Place.{}".format(
                pla.id), storage.all().keys())


class TestPlaceDotNotation(unittest.TestCase):
    """Testing the `place` command's dot notation."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_count_place(self):
        """Test count place object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Place.count()'))
            counter = 0
            for i in storage.all().values():
                if type(i) is Place:
                    counter += 1
            self.assertEqual(int(f.getvalue()), counter)

    def test_all_place(self):
        """Test all place object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Place.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Place]')

    def test_show_place(self):
        """Test show place object."""
        with patch('sys.stdout', new=StringIO()) as f:
            pla = Place()
            pla.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.show("{pla.id}")'))
            res = f"[{type(pla).__name__}] ({pla.id}) {pla.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_place(self):
        """Test update place object."""
        with patch('sys.stdout', new=StringIO()) as f:
            pla = Place()
            pla.name = "MOSTAFA"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.update("{pla.id}", name, "Ife")'))
            self.assertEqual(pla.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            pla = Place()
            pla.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.update("{pla.id}", age, 25)'))
            self.assertIn("age", pla.__dict__.keys())
            self.assertEqual(pla.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            pla = Place()
            pla.age = 60
            cmmd = f'Place.update("{pla.id}", age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", pla.__dict__.keys())
            self.assertNotIn("color", pla.__dict__.keys())
            self.assertEqual(pla.__dict__["age"], 10)

    def test_update_place_dict(self):
        """Test update place object."""
        with patch('sys.stdout', new=StringIO()) as f:
            pla = Place()
            pla.age = 75
            cmmd = f'Place.update("{pla.id}", {{"age": 25, "color": "black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(pla.__dict__["age"], 25)
            self.assertIsInstance(pla.__dict__["age"], int)

    def test_destroy_place(self):
        """Test destroy place object."""
        with patch('sys.stdout', new=StringIO()):
            pla = Place()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.destroy("{pla.id}")'))
            self.assertNotIn("Place.{}".format(
                pla.id), storage.all().keys())


class TestAmenity(unittest.TestCase):
    """Testing the `amenity` commands."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_amenity(self):
        """Test create amenity object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Amenity')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Amenity.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_amenity(self):
        """Test all amenity object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Amenity')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Amenity]')

    def test_show_amenity(self):
        """Test show amenity object."""
        with patch('sys.stdout', new=StringIO()) as f:
            ameni = Amenity()
            ameni.eyes = "green"
            HBNBCommand().onecmd(f'show Amenity {ameni.id}')
            res = f"[{type(ameni).__name__}] ({ameni.id}) {ameni.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_amenity(self):
        """Test update amenity object."""
        with patch('sys.stdout', new=StringIO()) as f:
            ame = Amenity()
            ame.name = "Cecilia"
            HBNBCommand().onecmd(f'update Amenity {ame.id} name "Ife"')
            self.assertEqual(ame.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            ame = Amenity()
            ame.age = 75
            HBNBCommand().onecmd(f'update Amenity {ame.id} age 25')
            self.assertIn("age", ame.__dict__.keys())
            self.assertEqual(ame.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            ame = Amenity()
            ame.age = 60
            cmmd = f'update Amenity {ame.id} age 10 color green)'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", ame.__dict__.keys())
            self.assertNotIn("color", ame.__dict__.keys())
            self.assertEqual(ame.__dict__["age"], 10)

    def test_destroy_amenity(self):
        """Test destroy amenity object."""
        with patch('sys.stdout', new=StringIO()):
            ame = Amenity()
            HBNBCommand().onecmd(f'destroy Amenity {ame.id}')
            self.assertNotIn("Amenity.{}".format(
                ame.id), storage.all().keys())


class TestAmenityDotNotation(unittest.TestCase):
    """Testing the `amenity` command's dot notation."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_count_amenity(self):
        """Test count amenity object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Amenity.count()'))
            counter = 0
            for i in storage.all().values():
                if type(i) is Amenity:
                    counter += 1
            self.assertEqual(int(f.getvalue()), counter)

    def test_all_amenity(self):
        """Test all amenity object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Amenity.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Amenity]')

    def test_show_amenity(self):
        """Test show amenity object."""
        with patch('sys.stdout', new=StringIO()) as f:
            ame = Amenity()
            ame.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.show("{ame.id}")'))
            res = f"[{type(ame).__name__}] ({ame.id}) {ame.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_amenity(self):
        """Test update amenity object."""
        with patch('sys.stdout', new=StringIO()) as f:
            ame = Amenity()
            ame.name = "MOSTAFA"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.update("{ame.id}", name, "Ife")'))
            self.assertEqual(ame.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            ame = Amenity()
            ame.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.update("{ame.id}", age, 25)'))
            self.assertIn("age", ame.__dict__.keys())
            self.assertEqual(ame.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            ame = Amenity()
            ame.age = 60
            cmmd = f'Amenity.update("{ame.id}", age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", ame.__dict__.keys())
            self.assertNotIn("color", ame.__dict__.keys())
            self.assertEqual(ame.__dict__["age"], 10)

    def test_update_amenity_dict(self):
        """Test update amenity object."""
        with patch('sys.stdout', new=StringIO()) as f:
            ame = Amenity()
            ame.age = 75
            cmmd = f'Amenity.update("{ame.id}", {{"age": 25,\
                                    "color": "black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(ame.__dict__["age"], 25)
            self.assertIsInstance(ame.__dict__["age"], int)

    def test_destroy_amenity(self):
        """Test destroy amenity object."""
        with patch('sys.stdout', new=StringIO()):
            ame = Amenity()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.destroy("{ame.id}")'))
            self.assertNotIn("Amenity.{}".format(
                ame.id), storage.all().keys())


class TestCity(unittest.TestCase):
    """Testing the `city` commands."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_city(self):
        """Test create city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("City.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_city(self):
        """Test all city object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all City')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[City]')

    def test_show_city(self):
        """Test show city object."""
        with patch('sys.stdout', new=StringIO()) as f:
            ctyo = City()
            ctyo.eyes = "green"
            HBNBCommand().onecmd(f'show City {ctyo.id}')
            res = f"[{type(ctyo).__name__}] ({ctyo.id}) {ctyo.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_city(self):
        """Test update city object."""
        with patch('sys.stdout', new=StringIO()) as f:
            ctyo = City()
            ctyo.name = "MOSTAFA"
            HBNBCommand().onecmd(f'update City {ctyo.id} name "Ife"')
            self.assertEqual(ctyo.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            ctyo = City()
            ctyo.age = 75
            HBNBCommand().onecmd(f'update City {ctyo.id} age 25')
            self.assertIn("age", ctyo.__dict__.keys())
            self.assertEqual(ctyo.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            ctyo = City()
            ctyo.age = 60
            cmmd = f'update City {ctyo.id} age 10 color green'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", ctyo.__dict__.keys())
            self.assertNotIn("color", ctyo.__dict__.keys())
            self.assertEqual(ctyo.__dict__["age"], 10)

    def test_destroy_city(self):
        """Test destroy city object."""
        with patch('sys.stdout', new=StringIO()):
            ctyo = City()
            HBNBCommand().onecmd(f'destroy City {ctyo.id}')
            self.assertNotIn("City.{}".format(
                ctyo.id), storage.all().keys())


class TestCityDotNotation(unittest.TestCase):
    """Testing the `city` command's dot notation."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_count_city(self):
        """Test counter city object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('City.count()'))
            counter = 0
            for i in storage.all().values():
                if type(i) is City:
                    counter += 1
            self.assertEqual(int(f.getvalue()), counter)

    def test_all_city(self):
        """Test all city object."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('City.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[City]')

    def test_show_city(self):
        """Test show city object."""
        with patch('sys.stdout', new=StringIO()) as f:
            ctyob = City()
            ctyob.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.show("{ctyob.id}")'))
            res = f"[{type(ctyob).__name__}] ({ctyob.id}) {ctyob.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_city(self):
        """Test update city object."""
        with patch('sys.stdout', new=StringIO()) as f:
            ctyob = City()
            ctyob.name = "MOSTAFA"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.update("{ctyob.id}", name, "Ife")'))
            self.assertEqual(ctyob.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            ctyob = City()
            ctyob.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.update("{ctyob.id}", age, 25)'))
            self.assertIn("age", ctyob.__dict__.keys())
            self.assertEqual(ctyob.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            ctyob = City()
            ctyob.age = 60
            cmmd = f'City.update("{ctyob.id}", age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", ctyob.__dict__.keys())
            self.assertNotIn("color", ctyob.__dict__.keys())
            self.assertEqual(ctyob.__dict__["age"], 10)

    def test_update_city_dict(self):
        """Test update city object."""
        with patch('sys.stdout', new=StringIO()) as f:
            cb = City()
            cb.age = 75
            cmmd = f'City.update("{cb.id}", {{"age": 25, "color": "black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(cb.__dict__["age"], 25)
            self.assertIsInstance(cb.__dict__["age"], int)

    def test_destroy_city(self):
        """Test destroy city object."""
        with patch('sys.stdout', new=StringIO()):
            ctyoby = City()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.destroy("{ctyoby.id}")'))
            self.assertNotIn("City.{}".format(
                ctyoby.id), storage.all().keys())
