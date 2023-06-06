from turtle import Turtle, Screen
from random import random
turt = Turtle()

for i in range(3, 11):
    ang = 360 / i
    turt.color(random(), random(), random())
    while i > 0:
        turt.right(ang)
        turt.forward(100)
        i -= 1


screen = Screen()
screen.exitonclick()
