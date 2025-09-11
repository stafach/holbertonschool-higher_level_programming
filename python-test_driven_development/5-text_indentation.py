#!/usr/bin/python3
"""
This module define a function that print a text with 2 new lines
after each of these characters: ., ? and :
It check if that the inputs are string befor print the name.
"""


def text_indentation(text):
    """Print a text with 2 new line after .?: charaters

    Args:
        text (str): the text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        char = text[i]
        if char in "?:.":
            print(char, end="")
            print("\n")
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        else:
            print(char, end="")
        i += 1
