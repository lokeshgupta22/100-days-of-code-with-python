from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.writesc()

    def writesc(self):
        self.clear()
        self.goto(-210, 250)
        self.write(f"Level : {self.score}", align="center", font=FONT)

    def pointadd(self):
        self.score += 1
        self.writesc()

    def gameover(self):
        self.setpos(x=0, y=0)
        self.write("GAME OVER!", False, align="center", font=FONT)
