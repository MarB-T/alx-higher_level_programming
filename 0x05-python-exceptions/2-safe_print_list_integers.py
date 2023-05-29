#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    if my_list is None or x < 0:
        return (0)
    for item in range(0, x):
        try:
            print("{:d}".format(my_list[item]), end="")
            i += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (i)
