#!/usr/bin/env python3
"""
This module defines an abstract class Shape
and two subclasses Circle and Rectangle.
"""


from abc import ABC, abstractmethod

from math import pi


class Shape(ABC):
    """
    class named Shape using the ABC package
    """

    @abstractmethod
    def area(self):
        """
        abstact methode
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        abstact methode
        """
        pass


class Circle(Shape):
    """
    class named Circle inherits from Shape
    """
    def __init__(self, radius=0):
        """
        Args:
            radius: the radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        Return:
            The area of the circle
        """
        r = self.radius ** 2
        return r * pi

    def perimeter(self):
        """
        Return:
            The perimeter of the circle
        """
        return self.radius * 2 * pi


class Rectangle(Shape):
    """
    class named Rectangle inherits from Shape
    """
    def __init__(self, width=0, height=0):
        """
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Return:
            The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return:
            The perimeter of the rectangle
        """
        return (self.width + self.height) * 2


def shape_info(shape):
    """
    Args:
        shape: the name of the class
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
