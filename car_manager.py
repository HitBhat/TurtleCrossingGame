COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
import time


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=3)
        self.color(random.choice(COLORS))
        self.penup()
        self.number = 0
        self.goto(x=random.randint(260, 320), y=random.randint(-280, 240))
        self.speed("fastest")


    def movethecars(self):
        self.goto(x=self.xcor()-STARTING_MOVE_DISTANCE, y=self.ycor())













