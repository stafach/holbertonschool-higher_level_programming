#!/usr/bin/python3
def uppercase(str):
    result = ""
    for character in str:
        ordinal = ord(character) - 32
        if 65 <= ordinal <= 90:
            result += chr(ordinal)
        else:
            result += character
    print("{}" .format(result))
