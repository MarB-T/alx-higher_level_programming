#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        print("")
        return None
    for lis in matrix:
        for item in lis:
            if item == lis[-1]:
                print("{:d}".format(item))
            else:
                print("{:d}".format(item), end=' ')
