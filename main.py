from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(1)
paddle_2 = Paddle(2)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detection with the wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detection with paddle 1 and 2
    if (ball.xcor() >= 320 and ball.distance(paddle_1) < 50) or (ball.xcor() <= -320 and ball.distance(paddle_2) < 50):
        ball.bounce_x()

    # Detection when paddle 1 misses the ball
    if ball.xcor() >= 350:
        ball.goto(0, 0)
        ball.bounce_x()
        ball.move_speed = 0.1
        scoreboard.l_point()

    # Detection when paddle 2 misses the ball
    if ball.xcor() <= -350:
        ball.goto(0, 0)
        ball.bounce_x()
        ball.move_speed = 0.1
        scoreboard.r_point()

screen.exitonclick()