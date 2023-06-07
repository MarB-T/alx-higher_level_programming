#!/usr/bin/python3
""" Divides a matrix by a given number """

def matrix_divided(matrix, div):
    """
    function to divide matrix

    Args:
        matrix: the matrix, list of lists of int/floats
        div: the dividend

    Returns: a new matrix of the results
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if (not isinstance(matrix, list)
        or matrix == []
        or not all(isinstance(num, list) for num in matrix)
        or not all((isinstance(elem, int))
                   or (isinstance(elem, float))
                   for elem in [a for b in matrix for a in b])):
        raise TypeError("matrix must be a matrix (list of lists)\
        of integers/floats")
    if not (all(len(a) == len(matrix[0]) for a in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    return ([list(map((lambda x: round(x / div, 2)), row)) for row in matrix])
