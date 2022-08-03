#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    lister = []
    count = 1
    for x in range(0, n):
        sub = []
        for y in range(0, count):
            if x == 0:
                sub = [1]
                break
            elif x == 1:
                sub = [1, 1]
                break
            else:
                if y == 0 or y == count-1:
                    sub.append(1)
                else:
                    sub.append(lister[x-1][y-1] + lister[x-1][y])
        lister.append(sub)
        count = len(sub) + 1
    return lister
