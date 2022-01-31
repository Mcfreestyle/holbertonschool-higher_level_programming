#!/usr/bin/python3
"""This module supplies `is_same_class` function
"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class

    Args:
        obj: object
        a_class: specified class
    """
    return type(obj) is a_class
