#!/usr/bin/python3
"""This module defines a square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """
        Initialize the size attribute of the square

        Args:
            size (:obj:`int`, optional): size of the square

        """
        self.size = size

    @property
    def size(self):
        """The __size getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        The __size setter

        Args:
            value: size of the square

        Raises:
            TypeError: If value is not integer
            VaueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            the area of the square
        """
        area = self.__size ** 2
        return (area)
