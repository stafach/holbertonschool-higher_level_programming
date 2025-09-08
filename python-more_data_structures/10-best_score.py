#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = 0
        for cle in a_dictionary:
            if a_dictionary[cle] > max:
                max = a_dictionary[cle]
                key = cle
        return key
