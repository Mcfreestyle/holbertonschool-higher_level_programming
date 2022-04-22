#!/usr/bin/python3
"""This module supplies the `find_peak` function"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    sorted_list = sorted(list_of_integers, reverse=True)
    if len(sorted_list) > 0:
        return (sorted_list[0])
    else:
        return (None)
