#!/usr/bin/env python3
"""
This module design two mixin classes SwimMixin
and FlyMixin. A class Dragon inherits from both these mixins
"""


class SwimMixin:
    """
    Mixin called SwimMixin
    """
    def swim(self):
        """
        print a string
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin called FlyMixin
    """
    def fly(self):
        """
        print a string
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    class named Dragon that inherits from
    SwimMixin and FlyMixin
    """

    def roar(self):
        """
        print a string
        """
        print("The dragon roars!")
