#!/usr/bin/python3
"""
This module explore serialization and deserialization
using XML as an alternative format to JSON.
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Args:
        dictionary: Python dictionary
        filename: name of the file where we will save xml
    """
    data = ET.Element('data')

    for key in dictionary:
        ET.SubElement(data, key).text = dictionary[key]

    tree = ET.ElementTree(data)
    tree.write(filename, encoding='utf-8')


def deserialize_from_xml(filename):
    """
    Args:
        filename: the file to deserialize

    Return:
        A dictionnary
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dic = {}
    for elem in root:
        dic[elem.tag] = elem.text

    return dic
