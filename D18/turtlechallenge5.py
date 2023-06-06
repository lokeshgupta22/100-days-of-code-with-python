import turtle as t
import random

turt = t.Turtle()
t.colormode(255)


def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


turt.speed("fastest")
lim = 50
for j in range(lim):
    ang = 360/lim
    i = j*ang
    turt.setheading(i)
    turt.color(randomcolor())
    turt.circle(100)

'''for i in range(200):
    turt.color(randomcolor())
    turt.forward(30)
    turt.setheading(random.choice(directions))'''

screen = t.Screen()
screen.exitonclick()
