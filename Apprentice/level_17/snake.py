from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
TURNING_ANGLE = [0, 90, 180, 270]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != TURNING_ANGLE[3]:
            self.head.setheading(TURNING_ANGLE[1])

    def down(self):
        if self.head.heading() != TURNING_ANGLE[1]:
            self.head.setheading(TURNING_ANGLE[3])

    def right(self):
        if self.head.heading() != TURNING_ANGLE[2]:
            self.head.setheading(TURNING_ANGLE[0])

    def left(self):
        if self.head.heading() != TURNING_ANGLE[0]:
            self.head.setheading(TURNING_ANGLE[2])
