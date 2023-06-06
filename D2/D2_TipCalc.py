import numpy as np
import pandas as pd
print("Welcome to the Tip Calculator")
bill = float(input("What was your total bill? "))
n = int(input("How many people to split the bill? "))
tip = int(input("What percentage would you like to tip? "))
bill = bill + ((tip*bill)/100)
print(f"Each person should pay: {round((bill/n),2)}")
