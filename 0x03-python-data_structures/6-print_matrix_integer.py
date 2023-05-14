#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lis in matrix:
        for item in lis:
            if item == len(lis):
                print("{}".format(item))
            else:
                print("{}".format(item), end=' ')
        print()
