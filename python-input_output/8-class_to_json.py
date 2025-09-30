#!/usr/bin/python3
"""
This module define a function that
returns the JSON representation of an object
"""


def class_to_json(obj):
    """
    Args:
        my_obj: the object

    Return:
        the JSON representation of the object
    """
    return obj.__dict__
