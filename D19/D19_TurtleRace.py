from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
allturtles = []

yc = -90
for c in colors:
    turt = Turtle(shape="turtle")
    turt.color(c)
    turt.penup()
    turt.goto(x=-230, y=yc)
    allturtles.append(turt)
    yc += 30

user_bet = screen.textinput(
    title="Make your Bet.", prompt="Which turtle will win the race. Enter colour:")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in allturtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You Won! The winner is {winner}")
            else:
                print(f"You Lost! The winner is {winner}")

        steps = random.randint(0, 10)
        turtle.forward(steps)

screen.exitonclick()
