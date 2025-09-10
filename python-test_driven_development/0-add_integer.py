#!/usr/bin/python3
"""
This module defines a function that adds two numbers.
It checks that the inputs are integers or floats before adding them.
Floats are cast to integers before performing the addition.
"""


def add_integer(a, b=98):
    """
    Add two numbers and return the result as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
