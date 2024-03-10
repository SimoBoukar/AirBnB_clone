#!/usr/bin/python3
"""Create a Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place Class that inherit from BaseModel"""
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_bathrooms = 0
    price_by_night = 0
    number_rooms = 0
    longitude = 0.0
    latitude = 0.0
    max_guest = 0
    amenity_ids = []
