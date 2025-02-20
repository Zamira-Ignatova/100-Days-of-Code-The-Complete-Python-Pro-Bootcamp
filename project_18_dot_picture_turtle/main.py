import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

lily = Turtle()
lily.speed("fastest")
lily.shape("turtle")
lily.home()
lily.hideturtle()
rgb_colours = [(203, 165, 108), (37, 99, 133), (126, 83, 54), (127, 164, 189), (233, 206, 107), (173, 149, 42),
                (199, 75, 111), (223, 127, 145), (141, 55, 74), (119, 39, 70), (57, 46, 43), (86, 169, 116),
                (221, 67, 53), (105, 196, 190), (245, 160, 170), (66, 108, 77), (42, 157, 203), (2, 61, 85),
                (60, 53, 58), (214, 182, 177), (88, 50, 45), (153, 212, 198), (126, 119, 159), (60, 56, 103),
                (17, 89, 100), (160, 205, 215), (87, 86, 34), (187, 189, 203), (35, 89, 89)]

def dot_line():
    for i in range (10):
        lily.dot(20, (random.choice(rgb_colours)) )
        lily.penup()
        lily.forward(50)
        lily.pendown()


def dot_picture():
    y = 0
    for item in range (10):
        dot_line()
        y = y + 50
        lily.teleport(0, y)

dot_picture()

screen = Screen()
screen.exitonclick()
