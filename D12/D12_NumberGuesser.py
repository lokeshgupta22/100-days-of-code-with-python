import random

print("Welcome to the Number Guessing Game!")
num = random.randint(1, 100)
print("I am thinking of a number between 1 and 100")
print(num)
ch = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
lives = 0
if ch == 'easy':
    lives = 10
elif ch == 'hard':
    lives = 5
else:
    print("Invalid Input!")
while lives >= 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if num == guess:
        print("You Win!")
        exit()
    elif guess > num:
        print("Too High")
    elif guess < num:
        print("Too Low")
    if lives == 0:
        print(f"Game Over. The number was {num}")
        exit()
    print("Guess Again.")
    lives -= 1
