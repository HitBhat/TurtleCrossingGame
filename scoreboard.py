FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.writethescore()

    def writethescore(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(x=-200, y=250)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def increasescore(self):
        self.level += 1
        self.writethescore()

    def gameover(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over", align="center", font=FONT)




