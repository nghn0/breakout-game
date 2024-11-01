from turtle import Turtle


class Blocks(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("White")
        self.setpos((x, y))
