#!/usr/bin/python3
"""
This module create a classe named class
"""


class Square:
    """
create a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize a square with a private size

        Args:
            self: the square
            size (int): the size of the square

        Raises:
            TypeError: if size isn't an integer
            ValueError: if size is negative
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Getter for the position attribute.

        Returns:
            tuple of int: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the size attribute with validation.

        Args:
            value (int): The new position of the square.

        Raises:
            TypeError: if value is not an tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        print the square
        """
        if self.size == 0:
            print("")
        for x in range(0, self.__position[1]):
            print("")

        for i in range(0, self.size):
            for y in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.size):
                print("#", end="")
            print("")
