#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./Mycalculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    print(op)

    if op == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
    elif op == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
    elif op == "*":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))
    elif op == "/":
        if b == 0:
            print("Error: division by zero")
            exit(1)
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
    else:
        print(f"Unknown operator: {op}. Available operators: +, -, * and / ")
        exit(1)