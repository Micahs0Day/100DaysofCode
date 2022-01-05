from scoreboard import ScoreBoard
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time


# Screen setup
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

# Paddle Objects
left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)

# Ball Object
ball = Ball()

# Scoreboard object
scoreboard = ScoreBoard()

# Movement
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    # Detects collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detects collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.inc_left_score()

    # Detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.inc_right_score()

    if scoreboard.left_score == 10 or scoreboard.right_score == 10:
        game_on = False
        scoreboard.game_over()

screen.exitonclick()

