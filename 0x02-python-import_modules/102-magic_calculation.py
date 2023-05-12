#!/usr/bin/python3
add = __import__('magic_calculation_102').add
sub = __import__('magic_calculation_102').sub

def magic_function(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
