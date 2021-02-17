#!/usr/bin/python3
""" Module Base Class """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ Class to manage the database """
    def __init__(self, *args, **kwargs):
        """ Constructor """
        if len(kwargs) > 0:
            for key in kwargs.keys():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(kwargs[key],
                                              '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Return a srt respresentation"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ Update the public instance attribute updated_a """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Method return a new dictionary"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
