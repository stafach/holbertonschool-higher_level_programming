#!/usr/bin/python3
"""
This module define a function that creates
an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    Args:
        filename: the file

    Return:
        an object
    """
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)
    return obj
