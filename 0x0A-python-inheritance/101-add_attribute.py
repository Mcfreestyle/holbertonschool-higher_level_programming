#!/usr/bin/python3
"""This module supplies the ``add_attribute`` function
"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it's possible

    Args:
        obj: object
        name: name of the attribute
        value: value of the attribute

    Raises:
        TypeError: if the object can't have new attribute
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
