#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    for item in set_1:
        if item in set_2:
            continue
        else:
            new.append(item)
    for item in set_2:
        if item in set_1:
            continue
        else:
            new.append(item)

    return (new)
