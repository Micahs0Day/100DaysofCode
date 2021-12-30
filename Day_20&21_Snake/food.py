from turtle import Turtle
import random


color_list = ["lime", "blue", "green", "yellow", "pink", "orange", "teal", "white"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("pink")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.color(random.choice(color_list))
        self.goto(random_x, random_y)

