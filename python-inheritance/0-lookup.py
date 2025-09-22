#!/usr/bin/python3
"""
This module define a function that return the list
of available attributes and methods of an object
"""


def lookup(obj):
    """
    Args:
        obj: the object

    Return:
        the list of available attributes and methods of obj
    """
    return dir(obj)
