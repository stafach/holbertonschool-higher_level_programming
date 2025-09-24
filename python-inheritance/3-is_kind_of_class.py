#!/usr/bin/python3
"""
This module define that returns True if the object is an instance of,
or if the object is an instance of a class that
inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: the object
        a_class: the class

    Returns:
        True: if the object is an instance of the class
        False: if the object isn't an instance of the class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
