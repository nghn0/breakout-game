import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from block import Blocks
from points import Points

points = 0

screen = Screen()

screen.bgcolor("black")
screen.setup(height=600, width=1000)
screen.title("Breakout")

turtle.tracer(0)
pad = Paddle()

screen.listen()
screen.onkey(pad.mov_left, "Left")
screen.onkey(pad.mov_right, "Right")

ball = Ball()

blocks_list = []
y = 250
for i in range(0, 4):
    for j in range(-450, 500, 50):
        block = Blocks(j, y)
        blocks_list.append(block)
    y -= 50

pon = Points()

game_on = True
while game_on:
    turtle.update()
    ball.move()

    if points == 76:
        pon.won()
        break

    if ball.xcor() > 490 or ball.xcor() < -490:
        ball.bounce_x()

    if ball.ycor() > 290:
        ball.bounce_y()

    # Ball-paddle collision detection
    if ball.ycor() < -270 and ball.distance(
            pad) < 80 and ball.y_move < 0:  # Ensures ball is moving down and within paddle area
        ball.bounce_pad()

    if ball.ycor() < -300:
        pon.point(points)
        break

    for block in blocks_list:
        if ball.distance(block) < 20:
            block.hideturtle()  # Hide the block when hit
            blocks_list.remove(block)  # Remove the block from the list
            ball.bounce_y()  # Change ball's direction
            points += 1
            break  # Exit the loop early to avoid checking other blocks

screen.exitonclick()
