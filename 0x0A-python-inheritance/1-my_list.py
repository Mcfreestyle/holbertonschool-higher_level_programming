#!/usr/bin/python3
"""This module supplies the definition of a subclass
"""


class MyList(list):
    """Defines a method that prints a sorted list"""

    def print_sorted(self):
        """Prints a new sorted list"""
        print(sorted(self))
