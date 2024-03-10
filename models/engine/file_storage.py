#!/usr/bin/python3
"""Store object model"""
from json import dump, load
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

clsnametoobj = {
    'BaseModel' : BaseModel,
    'User' : User,
    'Amenity': Amenity,
    'City': City,
    'State': State,
    'Place': Place,
    'Review': Review
}

class FileStorage():
    """Create a File storage class."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj_dict = {}
        with open(FileStorage.__file_path, "w") as jsfile:
            for k,val in FileStorage.__objects.items():
                obj_dict[k] = val.to_dict()
            dump(obj_dict, jsfile)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as read_jsfile:
                desrl = load(read_jsfile)
                for obj in desrl.values():
                    cls_name = obj['__class__']
                    if cls_name in clsnametoobj:
                        cls_obj = clsnametoobj[cls_name]
                        self.new(cls_obj(**obj))

        except FileNotFoundError:
            pass
