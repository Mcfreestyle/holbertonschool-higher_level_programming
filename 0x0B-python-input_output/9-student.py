#!/usr/bin/python3
"""This module supplies the ``Student`` class
"""


class Student:
    """Definition of the class"""
    def __init__(self, first_name, last_name, age):
        """Initializes the instance
        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of a Student instance"""
        return (self.__dict__)
