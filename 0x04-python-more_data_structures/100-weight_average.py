#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    den = 0
    for item in my_list:
        num += (item[0] * item[1])
        den += item[1]
    return (num / den)
