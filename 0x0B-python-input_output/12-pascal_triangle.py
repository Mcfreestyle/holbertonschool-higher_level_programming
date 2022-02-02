#!/usr/bin/python3
"""This module supplies the ``pascal_triangle`` function
"""


def pascal_triangle(n):
    """Create a lists of lists of integers representing the Pascal's triangle
    Args:
        n: size of the triangle
    """
    if n <= 0:
        return ([])

    l1 = [[1]]
    l2 = []
    for i in range(1, n):
        l2 = [1] + [l2[i] + l2[i + 1] for i in range(len(l2) - 1)] + [1]
        l1.append(l2)
    return (l1)
