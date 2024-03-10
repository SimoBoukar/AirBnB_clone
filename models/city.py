#!/usr/bin/python3
"""Create a City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """ City Class that inherit from BaseModel"""
    name = ""
    state_id = ""
