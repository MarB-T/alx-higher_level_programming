#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    if my_list is None:
        return ('')
    if len(my_list) == 0:
        return ('')
    for ind in range(n - 1, -1, -1):
        print("{:d}".format(my_list[ind]))
