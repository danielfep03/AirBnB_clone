#!/usr/bin/python3
"""
    Test Module - FileStorage
"""

import unittest
from models.base_model import BaseModel
from models import storage
import os
import json


class AttributesTEst(unittest.TestCase):
    """ Tests __file_path and __objects """

    def test_file_storage(self):
        """ Tests atributes """

        mock = storage()
        self.assertIsNotNone(mock.__file_path)
        self.assertIsNotNone(mock.__objects)

class MethodsTest(unittest.TestCase):
    """ Tests all, new, save and reload """

    def test_all(self):
        """ Testing """
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """ Testing """

        mock = BaseModel()
        storage.new(mock)
        key = "{}.{}".format(mock.__class__.__name__, mock.id)
        self.assertTrue(storage.all()[key])

    def test_save(self):
        """ Testing """

        self.assertIsInstance(storage.all(), dict)
        dict1_size = len(storage.all())
        mock = BaseModel()
        mock.save()
        dict2_size = len(storage.all())
        self.assertNotEqual(dict1_size, dict2_size)

    def test_reload(self):
        """ Testing """

        list_size = len(storage.all())
        if os.path.isfile('file.json'):
            with open('file.json', 'r') as json:
                docu = json.read()
                storage.reload()
                storage.reload()
                self.assertGreater(list_size, 0)
