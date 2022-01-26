#!/usr/bin/python3
"""
This module supplies a function that prints a text
with 2 new lines after some characters
"""


def text_indentation(text):
    """ Prints a text with 2 new lines after each of these characters:
        ., ? and :

    Args:
        text: The text to print

    Raises:
        TypeError: If the text isn't a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    spc = 0
    text = text.strip()
    for i in range(len(text)):
        if text[i] == ' ' and spc == 1:
            continue
        spc = 0
        print(text[i], end='')
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            spc = 1
            print("\n")
