from turtle import Turtle

SHAPE = "turtle"
COLOR = "green"
PLAYER_START_POSITION = (0, -280)
WIDTH = 1
LENGTH = 1
MOVE_DISTANCE = 10
SPEED_SETUP = 0.1
FINISH_LINE = 260

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.color(COLOR)
        self.penup()
        self.y_move = MOVE_DISTANCE
        self.reset_position()
        self.speed_set_up = SPEED_SETUP
        self.finish_line = FINISH_LINE

    def move(self):
        new_y_coordinate = self.ycor() + self.y_move
        self.goto(0, new_y_coordinate)

    def reset_position(self):
        self.goto(PLAYER_START_POSITION)
        self.setheading(90)
        self.speed_set_up = SPEED_SETUP