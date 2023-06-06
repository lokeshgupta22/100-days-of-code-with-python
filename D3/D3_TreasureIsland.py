ta = "Y"
while ta == "Y":
    print("Welcome to the treasure island.\nYour Mission is to find the Treasure.")
    road = input(
        "You are at a cross road where do you want to go? Type 'left' or 'right'\n").lower()
    if road == "left":
        ch = input("You've come to a lake.There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
        if ch == "swim":
            print("You get attacked by an angry trout. GAME OVER.")
            ta = input("Do you want to Try Again? Press Y or N. ").upper()
        elif ch == "wait":
            tch = input(
                "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
            if tch == "red":
                print("It's a room full of fire. GAME OVER.")
                ta = input("Do you want to Try Again? Press Y or N. ").upper()
            elif tch == "yellow":
                print("You found the treasure! You WIN!")
                ta = input("Do you want to Play Again? Press Y or N. ").upper()
            elif tch == "blue":
                print("You enter a room of beasts. GAME OVER.")
                ta = input("Do you want to Try Again? Press Y or N. ").upper()
            else:
                print("Invalid")
                ta = input("Do you want to Try Again? Press Y or N. ").upper()
        else:
            print("Invalid")
            ta = input("Do you want to Try Again? Press Y or N. ").upper()
    elif road == "right":
        print("You fell into a hole. GAME OVER!")
        ta = input("Do you want to Try Again? Press Y or N. ").upper()
    else:
        print("Invalid")
        ta = input("Do you want to Try Again? Press Y or N. ").upper()
