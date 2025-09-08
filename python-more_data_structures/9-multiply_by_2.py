#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for cle in new:
        new[cle] *= 2
    return new
