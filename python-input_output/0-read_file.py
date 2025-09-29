#!/usr/bin/python3
"""
This module define a function that read a
text file and print it to stdout
"""


def read_file(filename=""):
    """
    Args:
        filename: the file to read
    """
    with open(filename, encoding="utf-8") as f:
        read = f.read()

        print(read, end="")
