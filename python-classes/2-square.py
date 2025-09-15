#!/usr/bin/python3
"""
This module create a classe named class
"""


class Square:
    """
create a square
    """
    def __init__(self, size=0):
        """
        initialize a square with a private size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
