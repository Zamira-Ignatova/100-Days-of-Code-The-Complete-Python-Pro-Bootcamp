from turtle import Turtle

MOVE_DISTANCE = 20
SHAPE = "square"
COLOR = "white"
WIDTH = 5
LENGTH = 1

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.color(COLOR)
        self.penup()
        self.goto(position)

    def go_up(self):
        y_coordinate = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_coordinate)

    def go_down(self):
        y_coordinate = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y_coordinate)

    