from higherlower_database import data
from higherlower_art import logo, vs
import random
import os


def select(a):
    name = a["name"]
    des = a["description"]
    country = a["country"]
    p = f"{name}, a {des}, from {country}"
    return p


'''def check(a, b, score):
    if a > b:
        print("You are right")
        score += 1
        print(score)
    else:
        print("You are wrong")
        print(f"Your final score {score}")
        exit()'''


def play():
    score = 0
    contd = True
    a = random.choice(data)
    while contd:
        print(logo)
        b = random.choice(data)
        if a == b:
            b = random.choice(data)
        print(f"Compare A: {select(a)}")
        print(vs)
        print(f"Against B: {select(b)}")
        guess = input("Who has more followers? Type A or B: ").lower()
        os.system("clear")
        fa = a["follower_count"]
        fb = b["follower_count"]
        if guess == "a":
            if fa > fb:
                print("You are right")
                a = b
                score += 1
                print(f"Your Current Score is {score}")
            else:
                print("You are wrong")
                print(f"Your final score was {score}")
                contd = False
        elif guess == "b":
            if fb > fa:
                print("You are right")
                a = b
                score += 1
                print(f"Your Current Score: {score}")
            else:
                print("You are wrong")
                print(f"Your final score was {score}")
                contd = False
        else:
            print("Invalid input")


play()
