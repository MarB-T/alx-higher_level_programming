#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        print()
    for lis in range(len(matrix)):
        for item in range(len(matrix[lis])):
            if item == len(matrix[lis]) - 1:
                print("{:d}".format(matrix[lis][item]))
            else:
                print("{:d}".format(matrix[lis][item]), end=' ')
