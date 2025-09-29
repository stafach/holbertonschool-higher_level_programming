#!/usr/bin/python3
"""
This module define a function that
returns an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    Args:
        my_str: the string

    Return:
        an object
    """
    obj = json.loads(my_str)
    return obj
