#!/usr/bin/python3

""" Storage - Object Production Module
        serialize and deserialize BaseModel Objects
        from .JSON to dictionary
        from dictionary to .JSON
        dictionary = "class_name.id": methods, attributes, numbers, 'strings'
        .JSON = '"class_name.id": "methods", "attributes", numbers, "strings"'
"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage():
        """ Information conversion between web server and user computer
                __filepath -> .json file location in web server
                __objects -> dictionary with relevant information about objects
                all -> returns the dictionary
                new -> adds a new key - object to the dictionary
                save -> serialization [from __filepath to __objects]
                reload -> deserialization [from __objects to __filepath]
        """

        __file_path = 'file.json'
        __objects = dict()

        def all(self):
            """ Return a dictionary """
            return FileStorage.__objects

        def new(self, obj):
            """ Return new dictionary """
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

        def save(self):
            """ Serialize a Json file """
            new_dict = dict()
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            with open(self.__file_path, "w") as json_file:
                json.dump(new_dict, json_file)

        def reload(self):
            """ Deserialize a Json file """
            try:
                with open(FileStorage.__file_path, "r") as json_file:
                    dict__objects = json.load(json_file)
                    for classname, dic in dict__objects.items():
                        self.__objects[classname] = eval(dic['__class__'])(**dic)
            except Exception:
                pass
