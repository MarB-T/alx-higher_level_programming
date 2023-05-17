#!/usr/bin/python3
def search_replace(mylist, search, replace):
    l = len(mylist)
    new_list = []
    for i in range(l - 1):
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(mylist[i])
    return (new_list)
