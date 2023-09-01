#!/usr/bin/python3
"""Find a Peak in a List"""
def find_peak(list_of_integers):
    """Find a Peak in a list """
    listt = list_of_integers
    l = len(listt)
    peaks = []
    if (l <= 2):
        return (None)
    for i in range(1, l - 1):
	    if (listt[i - 1] <= listt[i] >= listt[i + 1]):
	        peaks.append(listt[i])
    return (peaks)
