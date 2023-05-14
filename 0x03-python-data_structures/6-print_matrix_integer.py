#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print('\n')
    for lis in matrix:
        for item in range(len(lis)):
            if item == len(lis) -1:
                print("{:d}".format(lis[item]))
            else:
                print("{:d}".format(lis[item]), end=' ')
