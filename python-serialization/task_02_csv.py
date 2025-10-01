#!/usr/bin/python3
"""
This module reading data from one format (CSV) and
converting it into another format (JSON) using serialization techniques.
"""


import csv
import json


def convert_csv_to_json(filename):
    """
    Args:
        filename: the csv file to convert
    """
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            for row in reader:
                data.append(row)
    except Exception:
        return False

    try:
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile)
        return True
    except Exception:
        return False
