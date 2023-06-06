from turtle import Turtle, Screen
import random

turt = Turtle()
directions = [0, 90, 180, 270]
turt.pensize(15)
turt.speed("fastest")

for i in range(200):
    turt.color(random.random(), random.random(), random.random())
    turt.forward(30)
    turt.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
