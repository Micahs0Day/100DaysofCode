from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_score()

