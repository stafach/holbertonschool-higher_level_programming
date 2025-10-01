#!/usr/bin/python3
"""
This module create a class named CustomObject
"""


import pickle


class CustomObject:
    """
    calss named CustomObject
    """
    def __init__(self, name, age, is_student):
        """
        Args:
            name (str): name of the student
            age (int): age of the student
            is_student (bool): verification if it's a student or not
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        display a string
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Args:
            filename: file where we will serialize the
            current instance of of the object
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Args:
            filename: the file we deserialize
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (pickle.UnpicklingError, EOFError, FileNotFoundError):
            return None
