#!/usr/bin/python3
"""
This module define a function that append
a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Args:
        filename: the file to write
        text: the text to write

    Return:
        number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        write = f.write(text)
        return write
