#!/usr/bin/python3
"""
This module define a function that write
a string in a text file
"""


def write_file(filename="", text=""):
    """
    Args:
        filename: the file to write
        text: the text to write
    """
    with open(filename, "w", encoding="utf-8") as f:
        write = f.write(text)
        return write
