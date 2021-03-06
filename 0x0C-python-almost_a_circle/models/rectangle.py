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

    def __str__(self):
        """Returns description of the rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

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
        """The __width setter

        Raises:
            TypeError: if the width isn't integer
            ValueError: if the width is under or equals 0
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """The __height setter

        Raises:
            TypeError: if the height isn't integer
            ValueError: if the height is under or equals 0
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """The __x setter

        Raises:
            TypeError: if x isn't integer
            ValueError: if x is under 0
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """The __y setter

        Raises:
            TypeError: if y isn't integer
            ValueError: if y is under 0
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """Prints the rectangle"""

        for posy in range(self.y):
            print()
        for h in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Updates the attributes of the object"""

        argc = len(args)
        if argc > 5:
            argc = 5

        attrs = ["id", "width", "height", "x", "y"]
        if argc > 0:
            for i in range(argc):
                setattr(self, attrs[i], args[i])
            return

        for key, value in kwargs.items():
            if key in attrs:
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
