#!/usr/bin/python3
"""This module defines a square class"""


class Square:
    """square class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize size and position attributes of the square

        Args:
            size (:obj:`int`, optional): size of the square
            position(:obj:`tuple`, optional): position of the square

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """The __position getter"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """The __position setter"""
        try:
            if len(value) != 2:
                raise TypeError

            for i in range(2):
                if isinstance(value[i], int):
                    if value[i] < 0:
                        raise TypeError
                else:
                    raise TypeError
            self.__position = value
        except TypeError:
            print("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Calculates the area of the square

        Returns:
            the area of the square
        """
        area = self.__size ** 2
        return (area)

    def my_print(self):
        """ Prints a square with # """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for row in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
