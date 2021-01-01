STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__() # to call the constructor of the parent class
        self.shape("turtle")
        self.penup()
        self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])  # tuples allow us to use the index operator, moreover
        # we could just provide the tuple to the goto function as it also excepts a tuple (self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.goto(x=self.xcor(), y=self.ycor()+MOVE_DISTANCE)

    def resettheplayer(self):
        self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])



