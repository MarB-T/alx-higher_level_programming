#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    best = 0
    for key, value in a_dictionary.items():
        if value >= best:
            best_key = key
            best = value
    return (best_key)