from turtle import Turtle, Screen
import random

screen = Screen()
turt = Turtle()

turt.pensize(15)
turt.speed("fastest")

for i in range(100):
    r = random.randint(1, 2)
    # if ((round(turt.xcor(), 2) >= -200.00) & (round(turt.xcor(), 2) <= 200.00)) & ((round(turt.ycor(), 2) >= -200.00) & (round(turt.ycor(), 2) <= 200.00)):
    turt.forward(25)
    if r == 1:
        turt.right(90)
    else:
        turt.left(90)
    turt.color(random.random(), random.random(), random.random())
    # else:
    #     turt.right(90)
    #     turt.forward(25)


screen.exitonclick()
