from turtle import Turtle


class Ship(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.left(90)
        self.penup()
        self.goto(x=0, y=-350)
