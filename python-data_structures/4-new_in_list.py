#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()
    if idx < len(my_list) and idx > 0:
        new[idx] = element
    return new
