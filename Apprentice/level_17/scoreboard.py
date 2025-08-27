from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.write_title()

    def increase_score(self):
        self.score += 1
        self.write_title()

    def write_title(self):
        self.clear()
        self.write(
            f"Score:{self.score} High Score:{self.high_score}",
            align=ALIGMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_title()
