#!/usr/bin/python3

""" User Class - Module
        sets the follow parameters to the User:
            email
            password
            first_name
            last_name
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ User Class - Module"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
