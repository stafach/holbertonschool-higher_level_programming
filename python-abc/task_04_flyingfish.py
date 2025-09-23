#!/usr/bin/env python3
"""
This module defines a class named FlyingFish
that inherits from both a Fish class and a Bird class
"""


class Fish:
    """
    class named Fish
    """
    def swim(self):
        """
        print a string
        """
        print("The fish is swimming")

    def habitat(self):
        """
        print a string
        """
        print("The fish lives in water")


class Bird:
    """
    class named Bird
    """

    def fly(self):
        """
        print a string
        """
        print("The bird is flying")

    def habitat(self):
        """
        print a string
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    class named FlyingFish that inherits
    from Fish and Bird.
    """
    def fly(self):
        """
        print a string
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        print a string
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        print a string
        """
        print("The flying fish lives both in water and the sky!")
