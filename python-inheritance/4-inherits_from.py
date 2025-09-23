#!/usr/bin/python3
"""
This module define a function
that returns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: the object
        a_class: the class

    Returns:
        True: if the object is an instance of the class hat inherited
        (directly or indirectly) from the specified class
        False: if the object isn't an instance of the class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
