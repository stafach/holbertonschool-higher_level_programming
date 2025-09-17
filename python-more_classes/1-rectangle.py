#!/usr/bin/python3
"""
This module create a classe named rectangle
"""


class Rectangle:
    """
create a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initialize a rectangle with a private size

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle

        Raises:
            TypeError: if width or height aren't an integer
            ValueError: if width or height is negative
        """
        self._Rectangle__width = width
        self._Rectangle__height = height

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the square.
        """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the square.
        """
        return self._Rectangle__height

    @width.setter
    def height(self, value):
        """
        Setter for the height attribute with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
