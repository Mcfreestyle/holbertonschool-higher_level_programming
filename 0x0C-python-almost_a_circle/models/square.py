#!/usr/bin/python3
"""This module supplies the ``Square`` class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Definition of the class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the object

        Args:
            size: size of the square
            x: position x
            y: position y
            id: square id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the description of the square"""
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """The size getter"""
        return (self.width)

    @size.setter
    def size(self, value):
        """The size setter"""
        self.width = value
        self.height = value
