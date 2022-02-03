#!/usr/bin/python3
"""This module supplies the ``Rectangle`` class
"""
from models.base import Base


class Rectangle(Base):
    """Definition of the class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the object

        Args:
            width = rectangle width
            height = rectangle height
            x = position x
            y = position y
            id = rectangle id
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # ------- Getters ------ #
    @property
    def width(self):
        """The __width getter"""
        return (self.__width)

    @property
    def height(self):
        """The __height getter"""
        return (self.__height)

    @property
    def x(self):
        """The __x getter"""
        return (self.__x)

    @property
    def y(self):
        """The __y getter"""
        return (self.__y)

    # ---------- Setters --------- #
    @width.setter
    def width(self, value):
        """The __width setter"""
        self.__width = value

    @height.setter
    def height(self, value):
        """The __height setter"""
        self.__height = value

    @x.setter
    def x(self, value):
        """The __x setter"""
        self.__x = value

    @y.setter
    def y(self, value):
        """The __y setter"""
        self.__y = value
