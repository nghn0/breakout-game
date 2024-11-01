from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos((0, -221))
        self.x_move = 1
        self.y_move = 1

    def move(self):
        x, y = self.xcor(), self.ycor()
        self.goto((x + self.x_move, y + self.y_move))

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_pad(self):
        self.y_move *= -1
