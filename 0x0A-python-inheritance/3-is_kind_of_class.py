#!/usr/bin/python3
"""This module supplies the `is_kind_of_class` function
"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class

    Args:
        obj: object to check
        a_class: specified class
    """
    return (isinstance(obj, a_class))
