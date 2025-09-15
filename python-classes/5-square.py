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

        Args:
            self: the square
            size (int): the size of the square

        Raises:
            TypeError: if size isn't an integer
            ValueError: if size is negative
        """
        self._Square__size = size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        print the square
        """
        if self.size == 0:
            print("")
        for i in range(0, self.size):
            for j in range(0, self.size):
                print("#", end="")
            print("")
