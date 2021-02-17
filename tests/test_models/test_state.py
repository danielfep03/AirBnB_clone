#!/usr/bin/python3
"""
    Module Test to ckeck state
"""

import unittest
from models.base_model import BaseModel
from models.state import State
import uuid
import datetime


class AttributesTest(unittest.TestCase):
    """ Tests State's name """

    def test_state(self):
        """ tests name """

        mock = State()
        self.assertIsNotNone(mock.name)
