from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # high score
        with open("snakegamedata.txt") as file:
            self.high_score = file.read()
            self.high_score = int(self.high_score)
        self.penup()
        self.speed("fastest")
        self.pencolor("white")
        self.setpos(x=0, y=270)
        self.writesc()
        self.hideturtle()

    def update(self):
        self.score += 1
        self.writesc()

    def writesc(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}",
                   False, align=ALIGNMENT, font=FONT)

    # def gameover(self):
    #     self.setpos(x=0, y=0)
    #     self.write("GAME OVER!", False, align=ALIGNMENT, font=FONT)

    def resetsb(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.writesc()
