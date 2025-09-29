#!/usr/bin/python3
"""
This module define a function that
returns the JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """
    Args:
        my_obj: the object

    Return:
        the JSON representation of the object
    """
    json_str = json.dumps(my_obj)
    return json_str
