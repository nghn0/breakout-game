from turtle import Turtle


class Points(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto((-50, 0))

    def point(self, p):
        self.write(f"Points: {p}", font=("Arial", 30, "bold"))

    def won(self):
        self.write(f"YOU WON", font=("Arial", 30, "bold"))