#!/usr/bin/python3
"""
	Test Module for User
"""

import unittest
from models.base_model import BaseModel
from models.user import User
import uuid
import datetime


class AttributesTest(unittest.TestCase):
	""" Test assignation of user attributes """

	def test_place(self):
		""" test email password firs_name and last_name """

	mock = User()
	self.assertIsNotNone(mock.email)
	self.assertIsNotNone(mock.password)
	self.assertIsNotNone(mock.first_name)
	self.assertIsNotNone(mock.last_name)

