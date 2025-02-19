from turtle import Turtle

SHAPE = "circle"
COLOR = "white"
POSITION = (0, 0)
WIDTH = 1
LENGTH = 1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.color(COLOR)
        self.penup()
        self.goto(POSITION)
        self.x_move = 10
        self.y_move = 10
        self.speed_set = 0.1

    def move(self):
        new_y_coordinate = self.ycor() + self.y_move
        new_x_coordinate = self.xcor() + self.x_move
        self.goto(new_x_coordinate, new_y_coordinate)

    def bounce_y(self):
        self.y_move *= -1
        self.speed_set *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.home()
        self.bounce_x()
        self.speed_set = 0.1

