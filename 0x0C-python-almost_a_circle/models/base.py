#!/usr/bin/python3
"""This module supplies the ``Base`` class
"""
import json


class Base:
    """Definiion of the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the objects

        Args:
            id = id of the object
        """

        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))
