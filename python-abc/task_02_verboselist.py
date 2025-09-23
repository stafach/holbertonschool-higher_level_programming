#!/usr/bin/env python3
"""
This module defines a class named VerboseList
that extends the Python list class.
"""


class VerboseList(list):
    """
    class named VerboseList that inherits from
    the built-in list class.
    """

    def append(self, value):
        """
        append an item to the list and print a message

        Args:
            value: the value to append
        """
        super().append(value)
        print("Added [{}] to the list.".format(value))

    def extend(self, value):
        """
        extending the list and print a message

        Args:
            value: the value
        """
        super().extend(value)
        print("Extended the list with [{}] items.".format(len(value)))

    def remove(self, value):
        """
        removing the item from the list and print a message

        Args:
            value: the value to remove
        """
        super().remove(value)
        print("Removed [{}] from the list.".format(value))

    def pop(self, index=-1):
        """
        popping the item from the listand  print a message

        Args:
            value: the value to pop
        """
        value = super().pop(index)
        print("Popped [{}] from the list.".format(value))
        return value
