import random
from turtle import  Turtle

MOVE_DISTANCE = 20
SHAPE = "square"
SHAPE_HEAD = "circle"
COLOR = "white"
RESIZE_MODE = "user"
SPEED = "slowest"
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segments_list = []
        self.creating_snake()
        self.head = self.segments_list[0]
        self.head.shape(SHAPE_HEAD)
        self.head.shapesize(1, 2)

    def creating_snake(self):
        for position in STARTING_POSITION:
            self.add_segments(position)

    def add_segments(self, position):
        segment = Turtle()
        segment.shape(SHAPE)
        segment.resizemode(RESIZE_MODE)
        segment.color(COLOR)
        # segment.speed(SPEED)
        segment.penup()
        segment.goto(position)
        self.segments_list.append(segment)


    def extend(self):
        self.add_segments(self.segments_list[-1].position())

    def move(self):
        for each_segment in range((len(self.segments_list) - 1), 0, -1):
            new_x_coordinate = self.segments_list[each_segment - 1].xcor()
            new_y_coordinate = self.segments_list[each_segment - 1].ycor()
            self.segments_list[each_segment].goto(new_x_coordinate, new_y_coordinate)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset_snake(self):
        for item  in self.segments_list:
            item.hideturtle()
        self.segments_list.clear()
        self.creating_snake()
        self.head = self.segments_list[0]
        self.head.shape(SHAPE_HEAD)
        self.head.shapesize(1, 2)


