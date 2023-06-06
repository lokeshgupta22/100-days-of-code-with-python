from turtle import Turtle, Screen

turt = Turtle()

for i in range(15):
    turt.forward(10)
    turt.penup()
    turt.forward(10)
    turt.pendown()

screen = Screen()
screen.exitonclick()
