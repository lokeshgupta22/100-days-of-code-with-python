from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.allcars = []
        self.speed = STARTING_MOVE_DISTANCE

    def createcar(self):
        r = random.randint(1, 6)
        if r == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            newy = random.randint(-250, 240)
            car.setpos(x=310, y=newy)
            self.allcars.append(car)

    def movecar(self):
        for eachcar in self.allcars:
            eachcar.forward(self.speed)

    def levelup(self):
        self.speed += MOVE_INCREMENT
