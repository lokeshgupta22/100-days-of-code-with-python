import os
from calculator_art import logo
import time


def add(a, b): return a+b
def sub(a, b): return a-b
def mul(a, b): return a*b
def div(a, b): return a/b
def rem(a, b): return a % b


start = time.time()
print(logo)
k = 1
while k == 1:
    c = 1
    a = float(input("Enter first number: "))
    print("+\n-\n*\n/\n%")
    result = a
    while c == 1:
        op = input("Enter Operation: ")
        b = float(input("Enter second number: "))
        if op == "+":
            result = add(result, b)
            print(result)
        elif op == "-":
            result = sub(result, b)
            print(result)
        elif op == "*":
            result = mul(result, b)
            print(result)
        elif op == "/":
            if b == 0:
                print("Not Defined.")
            else:
                result = div(result, b)
                print(result)
        elif op == "%":
            result = rem(result, b)
            print(result)
        else:
            print("Invalid Input!")
        print(time.time()-start)
        contd = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, 'e' to exit: ")
        if contd == "y":
            c = 1
        elif contd == "n":
            c = 0
            os.system("clear")
        elif contd == "e":
            exit()
        else:
            print("Invalid Input!")
            c = 0
            os.system("clear")
