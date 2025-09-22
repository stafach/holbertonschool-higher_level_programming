#!/usr/bin/python3
"""
This module create a classe named BaseGeometry.
"""


class BaseGeometry:
    """
    class named BaseGeometry
    """

    def area(self):
        """
        calculate the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value

        Args:
            name (str): the name
            value (int): the value

        Raises:
            TypeError: If value isn't an integer
            ValueError: If value is negative
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
