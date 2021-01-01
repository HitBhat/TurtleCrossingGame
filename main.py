import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

screen.listen()
screen.onkey(player.move, "Up")

allcars = []


def create5cars():
    for i in range(5):
        car = CarManager()
        allcars.append(car)

create5cars()
scoreboard = Scoreboard()
scoreboard.writethescore()
game_is_on = True
createcars = True
speed = 0.1
while game_is_on:
    time.sleep(speed)
    screen.update()

    if allcars[len(allcars) - 1].xcor() <= 100:  # to be able to control the amount of cars on screen
        create5cars()

    # moving all the cars
    for cars in allcars:
        cars.movethecars()
        if player.distance(cars) < 15:
            print("player", player.ycor())
            print("cars", cars.ycor())
            scoreboard.gameover()
            game_is_on = False
            break

    # upgrade the level
    if player.ycor() >= 260:
        player.resettheplayer()
        speed *= 0.09
        scoreboard.increasescore()











screen.exitonclick()
