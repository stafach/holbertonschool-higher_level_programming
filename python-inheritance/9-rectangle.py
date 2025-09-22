#!/usr/bin/python3
"""
This module creates a Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        calculate the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string :"[Rectangle] <width>/<height>"
        """
        str = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return str
