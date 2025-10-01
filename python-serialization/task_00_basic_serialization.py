#!/usr/bin/python3
"""
This module a basic serialization module that adds the
functionality to serialize a Python dictionary to a JSON
file and deserialize the JSON file to recreate the Python Dictionary.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Args:
        filename: The filename of the input JSON file

    Return:
        a Python Dictionary with the deseialized JSON data from the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        dic = json.load(f)
    return dic
