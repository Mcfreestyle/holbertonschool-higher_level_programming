#!/usr/bin/python3
"""This module supplies the ``write_file`` function
"""


def write_file(filename="", text=""):
    """Writes a string to a text file
    Args:
        filename: name of the file to open
        text: string to write

    Returns:
        Number of characters written
    """

    with open(filename, mode='w', encoding='UTF-8') as f:
        chr_written = f.write(text)
    return (chr_written)
