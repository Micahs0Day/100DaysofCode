import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
cars = CarManager()

screen.onkey(player.move_player, "Up")
screen.listen()
screen.bgpic("turtlecrossing.png")


game_is_on = True
x = 0

while game_is_on:

    time.sleep(0.075)
    screen.update()
    cars.move_cars()
    x += 1

    if x % 5 == 0:
        cars.create_cars()
    if player.ycor() > 240:
        scoreboard.inc_score()
        player.reset_player()
        cars.speed_up()

    for car in cars.cars:
        car_x = car.xcor()
        car_y = car.ycor()
        if player.distance(car_x, car_y - 8) < 20 or player.distance(car_x, car_y) < 20 \
                or player.distance(car_x - 10, car_y) < 20:
            screen.update()
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
