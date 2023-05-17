#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    best = next(iter(a_dictionary.values()))
    for key, value in a_dictionary.items():
        if value >= best:
            best_key = key
            best = value
    return (best_key)
