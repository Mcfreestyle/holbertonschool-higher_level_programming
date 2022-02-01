#!/usr/bin/python3
"""This module supplies the ``save_to_json_file``
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    Args:
        my_obj: object to write
        filename: name of the file
    """

    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(my_obj, f)
