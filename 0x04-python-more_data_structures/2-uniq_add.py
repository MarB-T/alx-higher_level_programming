#!/usr/bin/python3
def uniq_add(mylist=[]):
    check_list = []
    summ = 0
    for i in mylist:
        if i in check_list:
            continue
        else:
            summ += i
            check_list.append(i)

    return (summ)
