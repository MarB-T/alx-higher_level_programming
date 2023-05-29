#!/usr/bin/python3
def f(a, b):
    result = 0
    for i in range(1, 3):
        if i > a:
        raise Exception('Too far')
        result = result + a ** b / i
    result = result + b + a
    return result
