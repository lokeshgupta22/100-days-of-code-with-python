import random
import os
import time

words = ["life", "unfair", "success"]
r = random.randint(0, len(words)-1)
guess = words[r]
guess_list = []
blank_list = []
for i in range(len(guess)):
    blank_list.append("_")
    guess_list.append(guess[i])
blank_string = ""
for j in blank_list:
    blank_string += j
print("Word is: ", blank_string)
lives = 5

while "_" in blank_list:
    strb = ""
    ch = input("Enter guess: ")
    # time.sleep(1)
    # os.system("clear")
    for i in range(len(guess_list)):
        if ch in guess_list[i]:
            print(
                f"Correct guess! \nYour guess is present at {guess_list.index(ch)+1} position")
            blank_list[guess_list.index(ch)] = ch
            for j in blank_list:
                strb += j
            print(strb)
    if ch not in guess_list:
        lives -= 1
        print(f"Wrong Guess! \nYou lost a life.\nRemaining lives:{lives}")
        # print(strb)
        if lives == 0:
            print(f"Sorry no lives left.\nYour word was {guess}")
            exit()


print(f"You Won! \nYour word was {guess}")
