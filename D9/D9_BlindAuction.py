import os
from auction_art import logo
print(logo)
print("Welcome to the Blind Auction!")
c = 1
auction = {}
while c == 1:
    name = input("Enter Name: ")
    bid = int(input("Enter bid: $"))
    auction[name] = bid
    ch = input("Are there other bidders? Type y for Yes and n for No: ")
    if ch == "n":
        c = 0
    elif ch == "y":
        os.system("clear")
        c = 1
    else:
        print("Invalid Input!")
        c = 0
# print(auction)
max = 0
win = ""
for i in auction:
    if auction[i] >= max:
        win = i
        max = auction[i]
print(f"{win} wins the auction with a bid of ${max}")
