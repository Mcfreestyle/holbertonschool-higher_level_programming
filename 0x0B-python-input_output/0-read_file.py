#!/usr/bin/python3
"""This module supplies the ``read_file`` function
"""


def read_file(filename=""):
    """Reads a text file and prints it
    Args:
        filename = name of the file to open
    """

    with open(filename, mode='r', encoding='UTF-8') as f:
        print(f.read(), end='')
