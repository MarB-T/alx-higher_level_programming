#!/usr/bin/python3
def my_function(a, b):
    c = 0
    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
    else:
        c = sub(a, b)
    return c

