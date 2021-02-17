#!/usr/bin/python3
"""
    Test Module - Place
"""

import unittest
from models.base_model import BaseModel
from models.place import Place
import uuid
import datetime


class AttributesTest(unittest.TestCase):
    """ Test city_id, user_id, name, description, number_rooms,
        number_bathrooms, max_guest, price_by_night, latitude,
        longitude and amenity_ids
    """

    def test_place(self):

        dummy = Place()
        self.assertIsNotNone(mock.city_id)
        self.assertIsNotNone(mock.user_id)
        self.assertIsNotNone(mock.name)
        self.assertIsNotNone(mock.description)
        self.assertIsNotNone(mock.number_rooms)
        self.assertIsNotNone(mock.number_bathrooms)
        self.assertIsNotNone(mock.max_guest)
        self.assertIsNotNone(mock.price_by_night)
        self.assertIsNotNone(mock.latitude)
        self.assertIsNotNone(mock.longitude)
        self.assertIsNotNone(mock.amenity_ids)
