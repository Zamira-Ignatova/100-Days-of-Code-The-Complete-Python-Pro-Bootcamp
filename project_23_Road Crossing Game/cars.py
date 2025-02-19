import random
import turtle
from turtle import Turtle

turtle.colormode(255)

SHAPE = "square"
COLOR = "white"
WIDTH = 1
LENGTH = 2
STARTING_POSITIONS = [(320, -220), (320, -200),(320, -180), (320, -160), (320, -140), (320, -120), (320, -100),
                      (320, -80), (320, -60), (320, -40), (320, -20), (320, 0), (320, 220), (320, 200),(320, 180),
                      (320, 160), (320, 140), (320, 120), (320, 100), (320, 80), (320, 60), (320, 40), (320, 20)]

def color_of_cars():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_tuple = (r, g, b)
    return rgb_tuple

class Cars:

    def __init__(self):
        self.cars_list = []
        self.speed_set = 0.1
        self.move_distance = 10

    def creating_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.setheading(180)
        new_car.shape(SHAPE)
        new_car.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        new_car.color(color_of_cars())
        new_car.goto(random.choice(STARTING_POSITIONS))
        self.cars_list.append(new_car)

    def move_cars(self):
        for car in self.cars_list[::5]:
            car.forward(self.move_distance)

    def increasing_speed_of_cars(self):
        self.move_distance += 5


