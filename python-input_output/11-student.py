#!/usr/bin/python3
"""
This module define a class named Student
"""


class Student:
    """
    class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name: the first name of the student
            last_name: the last name of the student
            age: the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation
        of a Student instance
        """
        if isinstance(attrs, list):
            for string in attrs:
                if isinstance(string, str):
                    dic = {}
                    for key in attrs:
                        if hasattr(self, key):
                            dic[key] = getattr(self, key)
            return dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance

        Args:
            json: a dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
