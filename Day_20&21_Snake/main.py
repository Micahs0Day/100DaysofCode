from scoreboard import ScoreBoard
from turtle import Screen
from snake import Snake
from food import Food
import time

# Game Window setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Game Objects
scoreboard = ScoreBoard()
snake = Snake()
food = Food()

# Listens for Key input
screen.listen()

# Movement Keys
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Starts/Exits Game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision Detection w/ Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()

    # Collision Detection w/ Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Collision Detection w/ Body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()




