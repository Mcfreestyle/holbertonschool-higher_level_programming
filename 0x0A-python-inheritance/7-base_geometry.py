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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
