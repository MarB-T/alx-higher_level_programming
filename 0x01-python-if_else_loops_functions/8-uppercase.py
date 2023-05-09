#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 90 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")

