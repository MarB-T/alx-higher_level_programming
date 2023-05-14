#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        return None
    for lis in matrix:
        for item in lis:
            if item == lis[-1]:
                print("{:d}".format(item))
            else:
                print("{:d}".format(item), end=' ')
