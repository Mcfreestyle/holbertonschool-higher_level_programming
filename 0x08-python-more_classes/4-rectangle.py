#!/usr/bin/python3
"""
This module supplies a Rectangule class
"""


class Rectangle:
    """Defines the attributes, properties and methods
    """
    def __init__(self, width=0, height=0):
        """Defines the properties

        Args:
            width: width of the rectangule
            height: height of the rectangule
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """The __width getter"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """The __width setter

        Args:
            value: width of the rectangule

        Raises:
            TypeError: If the width isn't an integer
            ValueError: If the width isn't >= 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The __height getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """The __height setter

        Args:
            value: height of the rectangule

        Raises:
            TypeError: If the height isn't an integer
            ValueError: If the height isn't >= 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            Area of the rectangle
        """

        area = self.width * self.height
        return (area)

    def perimeter(self):
        """Calculate the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle
        """

        if self.width == 0 or self.height == 0:
            return (0)
        perimeter = 2 * self.width + 2 * self.height
        return (perimeter)

    def __str__(self):
        """Prints the rectangle

        Returns:
            String with characters '#'
        """

        rect = ""
        if self.width == 0 or self.height == 0:
            return (rect)

        for i in range(self.height):
            n = '\n' if i != self.height - 1 else ''
            rect += "#" * self.width + n
        return (rect)

    def __repr__(self):
        """Returns a string representation of the rectangle
        """

        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")
