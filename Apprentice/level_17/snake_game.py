from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_parts = []
for positions in starting_positions:
    snake_part = Turtle(shape="square")
    snake_part.color("white")
    snake_part.goto(positions)
    snake_parts.append(snake_part)
screen.exitonclick()
