import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("green")
        self.refresh()



    def refresh(self):
        random_x_coordinate = random.randint(-280, 280)
        random_y_coordinate = random.randint(-280, 280)
        self.goto(random_x_coordinate, random_y_coordinate)