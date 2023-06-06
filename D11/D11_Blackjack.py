from blackjack_art import logo
import random
import os


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def score(card):
    return sum(card)


def drawcard():
    return random.choice(cards)


def compare(pcards, ccards):
    if score(pcards) == 21 and len(pcards) == 2:
        print('\033[1m' + 'You Win with a Blackjack!' + '\033[0m')
    elif score(ccards) == 21 and len(ccards) == 2:
        print('\033[1m' + 'You Lose to a Blackjack!' + '\033[0m')
    elif score(ccards) > 21 and score(pcards) > 21:
        print('\033[1m' + 'You Lose' + '\033[0m')
        print(f"You Lose as your score reached {score(pcards)}")
    elif score(ccards) > 21:
        print('\033[1m' + 'You Win' + '\033[0m')
        print(f"You Win as computer's final score is {score(ccards)}")
    elif score(pcards) > 21:
        print('\033[1m' + 'You Lose' + '\033[0m')
        print(f"You lose as your final score is {score(pcards)}")
    elif score(pcards) > score(ccards):
        print('\033[1m' + 'You Win' + '\033[0m')
    elif score(pcards) < score(ccards):
        print('\033[1m' + 'You Lose' + '\033[0m')
    else:
        print('\033[1m' + 'It\'s a Draw!' + '\033[0m')


def new():
    new = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if new == 'y':
        os.system("clear")
        play()
    else:
        os.system("clear")
        print("Thanks for playing!")
        exit()


def play():
    contd = True
    print(logo)
    print("The Game starts now...")
    pcards = [drawcard(), drawcard()]
    #pcards = [11, 10]
    print(f"Your Cards are {pcards}, current score is {score(pcards)}")
    ccards = [drawcard(), drawcard()]
    #ccards = [11, 10]
    print(f"Computer's first card is {ccards[0]}")
    while contd:
        plus = input("Type 'y' to get another card or 'n' to pass: ")
        if plus == "y":
            chk = 11
            x = drawcard()
            pcards.append(x)
            if score(pcards) > 21 and chk in pcards:
                ind = pcards.index(11)
                pcards[ind] = 1
            if score(pcards) > 21:
                print('\033[1m' + 'You Lose' + '\033[0m')
                print(f"You Lose as your score reached {score(pcards)}")
                new()
            print(f"Your Cards are {pcards}, current score is {score(pcards)}")
            print(f"Computer's first card is {ccards[0]}")
        if plus == "n":
            print(
                f"Your final hand is {pcards}, final score is {score(pcards)}")
            while score(ccards) < 17:
                ccards.append(drawcard())
            print(
                f"Computer's final hand is {ccards}, final score is {score(ccards)}")
            compare(pcards, ccards)
            new()


play()
