#!/usr/bin/python3
"""This module supplies the ``append_write`` function
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    Args:
        filename: name of the file to open
        text: string to append

    Returns:
        Number of characters added
    """

    with open(filename, mode='a', encoding='UTF-8') as f:
        chr_added = f.write(text)
    return (chr_added)
