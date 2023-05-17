#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return (None)
    new_matrix = []
    for r in matrix:
        new_row = []
        for c in r:
            new_row.append(c * c)
        new_matrix.append(new_row)

    return (new_matrix)
