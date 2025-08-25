from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle win the race? Enter a color: "
).lower()
colors = ["blue", "red", "orange", "purple"]
y_position = [-25, -5, 15, 35]
teenage_mutant_ninja_turtles = []
for turtle_index in range(0, 4):
    teenage_mutant_ninja_turtle = Turtle(shape="turtle")
    teenage_mutant_ninja_turtle.penup()
    teenage_mutant_ninja_turtle.goto(x=-230, y=y_position[turtle_index])
    teenage_mutant_ninja_turtle.color(colors[turtle_index])
    teenage_mutant_ninja_turtles.append(teenage_mutant_ninja_turtle)


if user_bet:
    is_race_on = True
    while is_race_on:
        for turtle in teenage_mutant_ninja_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()
