#!/usr/bin/python3
""" script to implement pascal triangle """


def pascal_triangle(n):
    """pascal triangle function"""
    outer = []
    if n <= 0:
        return (outer)

    for row in range(n):
        outer.append([])
        outer[row].append(1)
        for j in range(1, row):
            outer[row].append(outer[row - 1][j - 1] + outer[row - 1][j])
        if (row != 0):
            outer[row].append(1)
    return (outer)

