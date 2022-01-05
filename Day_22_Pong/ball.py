from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0, 0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 5
        self.x_move = 5
        self.move_speed = 0.01

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= .9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= .9

    def reset_pos(self):
        self.setpos(0, 0)
        self.y_move *= -1
        self.x_move *= -1
