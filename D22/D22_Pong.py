import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboardpong import ScoreboardPong
import time

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


turt = t.Turtle()
turt.color("white")
turt.penup()
turt.setpos(x=0, y=-290)
turt.setheading(90)
turt.pendown()
for i in range(30):
    turt.forward(10)
    turt.penup()
    turt.forward(10)
    turt.pendown()

rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreboardPong()

screen.listen()
screen.onkey(fun=rpaddle.moveup, key="Up")
screen.onkey(fun=rpaddle.movedown, key="Down")

screen.onkey(fun=lpaddle.moveup, key="w")
screen.onkey(fun=lpaddle.movedown, key="s")


is_game_on = True
while is_game_on:
    time.sleep(ball.pace)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with paddle
    if (ball.xcor() > 320 and ball.distance(rpaddle) < 50) or (ball.xcor() < -320 and ball.distance(lpaddle) < 50):
        ball.play()

    # Detect missing the rpaddle
    if ball.xcor() > 380:
        ball.resetpos()
        scoreboard.lpoint()

    # Detect missing the lpaddle
    if ball.xcor() < -380:
        ball.resetpos()
        scoreboard.rpoint()

screen.exitonclick()
