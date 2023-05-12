#!/usr/bin/python3
from magic_calculation_102 import add, sub
def magic_calculation_102(a, b):
    c = 0
    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
    else:
        c = add(c, i)
    return c
