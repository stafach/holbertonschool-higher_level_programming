#!/usr/bin/env python3
"""
This module defines a class named CountedIterator
the built-in iterator obtained from the iter function.
"""


class CountedIterator:
    """
    class named CountedIterator
    """
    def __init__(self, data):
        """
        Args:
            data: the data to iter
        """
        self.iterator = iter(data)
        self.count = 0

    def get_count(self):
        """
        Return:
            a counter of items
        """
        return self.count

    def __next__(self):
        """
        Return:
            the next element of data
        """
        value = next(self.iterator)
        self.count += 1
        return value
