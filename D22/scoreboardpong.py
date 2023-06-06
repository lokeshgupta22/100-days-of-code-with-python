from turtle import Turtle


class ScoreboardPong(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.writescore()

    def lpoint(self):
        self.lscore += 1
        self.writescore()

    def rpoint(self):
        self.rscore += 1
        self.writescore()

    def writescore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))
