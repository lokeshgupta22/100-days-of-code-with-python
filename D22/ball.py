from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.pace = 0.1

    def move(self):
        newx = self.xcor()+self.xmove
        newy = self.ycor()+self.ymove
        self.goto(newx, newy)

    # def bounce(self):
    #     self.setheading((self.heading()+90))

    def bounce(self):
        self.ymove *= -1

    def play(self):
        self.xmove *= -1
        self.pace *= 0.9

    def resetpos(self):
        self.setpos(0, 0)
        self.xmove *= -1
        self.pace = 0.1
