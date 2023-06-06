import turtle as t

STEP = 20


class Snake:
    def __init__(self):
        self.allturt = []
        self.create_snake()
        self.head = self.allturt[0]

    def create_snake(self):
        xc = 0
        for i in range(3):
            self.add_segment((xc, 0))
            xc -= 20

    def add_segment(self, position):
        turt = t.Turtle(shape="square")
        turt.color("white")
        turt.penup()
        turt.setpos(position)
        self.allturt.append(turt)

    def resetsnake(self):
        for seg in self.allturt:
            seg.goto(1000, 1000)
        self.allturt.clear()
        self.create_snake()
        self.head = self.allturt[0]

    def extend(self):
        # add a new segment to the end of the snake
        self.add_segment(self.allturt[-1].position())

    def move(self):
        for turt_no in range((len(self.allturt)-1), 0, -1):
            newx = self.allturt[turt_no - 1].xcor()
            newy = self.allturt[turt_no - 1].ycor()
            self.allturt[turt_no].goto(newx, newy)
        self.head.forward(STEP)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
