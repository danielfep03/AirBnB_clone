#!/usr/bin/python3
"""
    Test Module - Review
"""

import unittest
from models.base_model import BaseModel
from models.review import Review
import uuid
import datetime


class AttributesTest(unittest.TestCase):
    """  Tests place_id user_id and text """

    def test_review(self):

        mock = Review()
        self.asserIsNotNone(mock.place_id)
        self.asserIsNotNone(mock.user_id)
        self.asserIsNotNone(mock.text)
