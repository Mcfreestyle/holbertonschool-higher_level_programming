#!/usr/bin/python3
"""
This module supplies one function that adds 2 numbers.
"""
def add_integer(a, b=98):
    """Adds 2 numbers

    Args:
        a: first number
        b: second number
    
    Raises:
        TypeError: If a or b are not integers or floats

    Returns:
        The sum of the 2 numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    res = int(a) + int(b)

    return (res)
