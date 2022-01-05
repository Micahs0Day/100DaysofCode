from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 245)
        self.right_score = 0
        self.left_score = 0
        self.update_score()

    def update_score(self):
        self.write(f"{self.left_score} | {self.right_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def inc_right_score(self):
        self.right_score += 1
        self.clear()
        self.update_score()

    def inc_left_score(self):
        self.left_score += 1
        self.clear()
        self.update_score()

