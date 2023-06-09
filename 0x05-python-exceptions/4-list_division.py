#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res = 0
    result = []
    i = 0

    while i < list_length:
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            result.append(res)
        i += 1
    return (result)
