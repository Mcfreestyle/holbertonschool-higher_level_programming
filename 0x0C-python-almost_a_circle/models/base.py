#!/usr/bin/python3
"""This module supplies the ``Base`` class
"""


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
