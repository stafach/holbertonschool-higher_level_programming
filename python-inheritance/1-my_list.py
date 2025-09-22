#!/usr/bin/python3
"""
This module create a classe named Mylist
"""


class MyList(list):
    """
    create a list that inherits from list
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
