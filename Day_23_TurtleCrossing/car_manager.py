import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        rand_car = Turtle()
        rand_x = random.randint(315, 375)
        rand_y = random.randint(-200, 240)
        rand_car.penup()
        rand_car.shape("square")
        rand_car.shapesize(1, 2)
        rand_car.setheading(180)
        rand_car.color(random.choice(COLORS))
        rand_car.goto(rand_x, rand_y)
        self.cars.append(rand_car)

    def speed_up(self):
        self.speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)





