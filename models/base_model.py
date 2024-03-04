#!/usr/bin/python3
"""Create a BaseModel Class"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel Class"""
    def __init__(self):
        """Initialization"""
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
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
