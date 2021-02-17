#!/usr/bin/python3

"""
	Test Module - City
"""

import unittest
from models.base_model import BaseModel
from models.city import City
import uuid
import datetime


class AttributesTest(unittest.TestCase):
	""" Tests state_id and name """

	def test_city(self):

		mock = City()
		self.assertIsNotNone(mock.state_id)
		self.assertIsNotNone(mock.name)

