from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.number = 0
        self.goto(x=300, y=random.randint(-250, 250))
        self.speed("fastest")



    def movethecars(self):
        self.goto(x=self.xcor()-STARTING_MOVE_DISTANCE, y=self.ycor())













