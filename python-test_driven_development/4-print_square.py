#!/usr/bin/python3
"""
This module define a function that print a square.
It check if that the input is a positive integer
"""


def print_square(size):
    """Prints a square

    Args:
        size (int): the size of the square

    Raises:
        TypeError: If size is a float and negative
        TypeError: If size is not an integer
        ValueError: If size < 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end=(""))
        print("")
