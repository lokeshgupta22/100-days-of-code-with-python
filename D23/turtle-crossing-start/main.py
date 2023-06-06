import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")
screen.onkey(fun=player.move, key="w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car.createcar()
    car.movecar()

    for eachcar in car.allcars:
        if player.distance(eachcar) < 20:
            game_is_on = False
            scoreboard.gameover()

    if player.finished():
        scoreboard.pointadd()
        player.resetplayer()
        car.levelup()

    screen.update()

screen.exitonclick()
