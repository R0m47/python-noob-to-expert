from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.take_highscore()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.write_title()

    def increase_score(self):
        self.score += 1
        self.write_title()

    def take_highscore(self):
        with open("Apprentice/level_17/data.txt") as file:
            return int(file.read())

    def update_highscore(self):
        with open("Apprentice/level_17/data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

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
            self.update_highscore()
        self.score = 0
        self.write_title()
