#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for cle in sorted(a_dictionary):
        print("{:s}: {}".format(cle, a_dictionary[cle]))
