#!/usr/bin/python3
"""
This module defines a class named Rectangle
"""


class Rectangle:
    """
    Class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with optional width and height.

        Args:
            width (int): the width of the rectangle (default 0).
            height (int): the height of the rectangle (default 0).
        """
        self.width = width    # goes through the setter
        self.height = height  # goes through the setter

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute with validation.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute with validation.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Compute and return the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Compute and return the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Return a string representation of the rectangle
        using the character '#'.
        If width or height is 0, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_p = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rectangle_p += "#"
            if i != self.__height - 1:
                rectangle_p += "\n"
        return rectangle_p

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used with eval() to recreate the instance.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message to indicate the rectangle is gone.
        """
        print("Bye rectangle...")
