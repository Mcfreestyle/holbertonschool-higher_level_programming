#!/usr/bin/python3
"""This module supplies the `Square` class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of the class"""
    def __init__(self, size):
        """Initializes the object

        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
