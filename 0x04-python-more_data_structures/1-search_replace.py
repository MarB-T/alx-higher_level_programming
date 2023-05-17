#!/usr/bin/python3
def search_replace(mylist, search, replace):
    length = len(mylist)
    new_list = []
    for i in range(length):
        if mylist[i] == search:
            new_list.append(replace)
        else:
            new_list.append(mylist[i])
    return (new_list)
