#!/usr/bin/python3
"""
	Test Module - Amenity
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import uuid
import datetime


class AttributesTest(unittest.TestCase):
	""" Tests name """

	def test_amenity(self):

		mock = Amenity()
		self.assertIsNotNone(mock.name)

