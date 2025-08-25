import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []
game_is_on = True

for positions in starting_positions:
    snake_segment = Turtle(shape="square")
    snake_segment.color("white")
    snake_segment.penup()
    snake_segment.goto(positions)
    snake_segments.append(snake_segment)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment in range(len(snake_segments) - 1, 0, -1):
        new_x = snake_segments[segment - 1].xcor()
        new_y = snake_segments[segment - 1].ycor()
        snake_segments[segment].goto(new_x, new_y)
    snake_segments[0].forward(20)


screen.exitonclick()
