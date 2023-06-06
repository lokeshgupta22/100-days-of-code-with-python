from random import randint
ta = "Y"
while ta == "Y":
    ch = int(input("Enter: "))  # 0-Rock 1-Paper 2-Scissors
    com = randint(0, 2)
    if ch == com:
        print(f"PLayer: {ch} and Computer: {com}")
        print("Draw")
    elif (ch == 0 and com == 2) or (ch == 1 and com == 0) or (ch == 2 and com == 1):
        print(f"PLayer: {ch} and Computer: {com}")
        print("Player wins")
    elif (ch == 2 and com == 0) or (ch == 0 and com == 1) or (ch == 1 and com == 2):
        print(f"PLayer: {ch} and Computer: {com}")
        print("Computer Wins")
    else:
        print("Please Enter Correct Number")
    ta = input("Do you want to Try Again? Press Y or N. ").upper()
