#!/usr/bin/python3
"""This module supplies the `inherits_from` function
"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Args:
        obj: object to check
        a_class: specified class
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
