#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    n = len(sys.argv) - 1
    summ = 0
    if n >= 1:
        for i in range(1, n + 1):
            summ = summ + int(sys.argv[i])
        print("{}".format(summ))
