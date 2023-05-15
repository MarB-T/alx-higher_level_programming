#!/usr/bin/python3
def check_tuple(tuple_a=()):
    list_c = []
    if len(tuple_a) == 0:
        list_c = [0, 0]
    elif len(tuple_a) == 1:
        list_c = [tuple_a[0], 0]
    else:
        list_c = [tuple_a[0], tuple_a[1]]

    return (list_c)


def add_tuple(tuple_a=(), tuple_b=()):
    list_d = check_tuple(tuple_a)
    list_e = check_tuple(tuple_b)
    a = list_d[0] + list_e[0]
    b = list_d[1] + list_e[1]
    list_f = [a, b]
    return (tuple(list_f))
