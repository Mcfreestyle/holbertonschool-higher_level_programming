#!/usr/bin/python3
"""This module supplies the `BaseGeometry` class
"""


class BaseGeometry:
    """Definition of the class"""
    def area(self):
        """Raises a Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raises exceptions

        Raises:
            TypeError: if value isn't an integer
            ValueError: if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
