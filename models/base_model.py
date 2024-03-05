#!/usr/bin/python3
"""Create a BaseModel Class"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        """Initialization"""
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dt_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, dt_obj)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Update the time."""
        self.updated_at = datetime.now()

    def __str__(self):
        """__str__ print objects info"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """Return dict"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        return new_dict
