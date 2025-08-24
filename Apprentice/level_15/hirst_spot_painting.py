import colorgram
import random
import turtle as t
from turtle import Screen


def create_color_list():
    rgb_colors = []
    colors = colorgram.extract("Apprentice/level_15/hirst_spot_painting.jpg", 20)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    return rgb_colors


def next_row():
    tim.left(90)
    tim.penup()
    tim.forward(30)
    tim.left(90)
    tim.forward(300)
    tim.right(180)


def create_hirst_spot_painting(color_list):
    for _ in range(10):
        for _ in range(10):
            tim.color(random.choice(color_list))
            tim.dot(20)
            tim.penup()
            tim.forward(30)
            tim.pendown()
        next_row()


colors = create_color_list()
tim = t.Turtle()
t.colormode(255)
create_hirst_spot_painting(colors)
screen = Screen()
screen.exitonclick()
