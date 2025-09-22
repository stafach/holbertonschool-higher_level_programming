#!/usr/bin/python3
"""
This module define a function
that returns True if the object is exactly an
instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: the object
        a_class: the class

    Returns:
        True: if the object is exactly an instance of the class
        False: if the object isn't an instance of the class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
