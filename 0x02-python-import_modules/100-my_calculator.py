#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import calculator_1 as calc

    n = len(sys.argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operators = "+-*/"
        op = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if op in operators:
            if op == '+':
                print("{} + {} = {}".format(a, b, calc.add(a, b)))
            elif op == '-':
                print("{} - {} = {}".format(a, b, calc.sub(a, b)))
            elif op == '*':
                print("{} * {} = {}".format(a, b, calc.mul(a, b)))
            elif op == '/':
                print("{} / {} = {}".format(a, b, calc.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

