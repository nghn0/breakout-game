from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=10)
        self.color("white")
        self.penup()
        self.setpos((0, -270))

    def mov_left(self):
        new_x = self.xcor() - 20
        if new_x >= -400:
            self.goto(new_x, self.ycor())

    def mov_right(self):
        new_x = self.xcor() + 20
        if new_x <= 400:
            self.goto(new_x, self.ycor())


