#!/usr/bin/python3
"""
This module supplies one function that prints the full name
"""


def say_my_name(first_name, last_name=""):
    """ Prints the full name

    Args:
        first_name: first name
        last_name: last name

    Raises:
        TypeError: If the first_name or last_name aren't strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
