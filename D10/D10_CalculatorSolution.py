import os
from calculator_art import logo
import time


def add(a, b): return a+b
def sub(a, b): return a-b
def mul(a, b): return a*b
def div(a, b): return a/b


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator():
    start = time.time()
    print(logo)
    a = float(input("Enter first number: "))
    for i in operations:
        print(i)
    c = True
    while c:
        op = input("Pick an operation: ")
        b = float(input("Enter next number: "))
        func = operations[op]
        answer = func(a, b)
        print(f"{a} {op} {b} = {answer}")
        print(time.time() - start)
        contd = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, 'e' to exit: ")
        if contd == "y":
            a = answer
        elif contd == "n":
            c = False
            calculator()
        else:
            exit()


calculator()
