#!/usr/bin/python3
"""This module defines a square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """
        Defines the size attribute of the square

        Args:
            size (:obj:`int`, optional): size of the square

        Raises:
            TypeError: If size is not integer
            VaueError: If size is less than 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
