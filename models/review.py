#!/usr/bin/python3

""" Review Class - Module
        sets the follow information to be Place parameters:
                place_id
                user_id
                text -> review of an specific user's place
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review Class - Module """
    place_id = ""
    user_id = ""
    text = ""
