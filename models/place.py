#!/usr/bin/python3
""" Place Class - Module
        sets the following information to a Place Instance:
                city_id -> city
                user_id -> user
                name -> place
                description -> place's description
                number_rooms
                number_bathrooms
                max_guest
                price_by_night
                latitude -> place's cardinality
                longitude -> place's cardinality
                amenity_ids -> amenities id
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """ Place Class - Module"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
