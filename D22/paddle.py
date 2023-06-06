from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(position)

    def moveup(self):
        newy = self.ycor() + 20
        self.setpos(x=self.xcor(), y=newy)

    def movedown(self):
        newy = self.ycor() - 20
        self.setpos(x=self.xcor(), y=newy)
