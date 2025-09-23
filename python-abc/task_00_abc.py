#!/usr/bin/env python3
"""
This module defines an abstract class Animal and two subclasses Dog and Cat.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    class named Animal
    """
    @abstractmethod
    def sound(self):
        """
        abstact methode for the class
        """
        pass


class Dog(Animal):

    def sound(self):
        """
        Return:
            the string Bark
        """
        return "Bark"


class Cat(Animal):

    def sound(self):
        """
        Return:
            the string Meow
        """
        return "Meow"
