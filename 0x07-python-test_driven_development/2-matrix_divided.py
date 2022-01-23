#!/usr/bin/python3
"""
This module supplies one function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix: matrix of numbers
        div: divider

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats
            or rows of the matrix are not the same size
            or div isn't a number(integer or float)
        ZeroDivisionError: If div is 0

    Returns:
        New matrix with divided elements
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError(msg)

    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(col / div, 2) for col in row]for row in matrix]

    return (new_matrix)
