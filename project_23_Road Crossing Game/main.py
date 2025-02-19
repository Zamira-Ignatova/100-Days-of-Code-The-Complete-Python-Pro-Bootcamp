from turtle import Screen
import time
from player import Player
from score_board import ScoreBoard
from cars import Cars

screen = Screen()
screen.setup(width=600, height=600, startx=0, starty=0)
screen.bgcolor("white")
screen.title("Road Crossing Game")
screen.tracer(0)

player = Player()
cars = Cars()
score_board = ScoreBoard()

screen.listen()
screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(player.speed_set_up)
    cars.creating_car()
    cars.move_cars()
    # detect collision with finish line to start a new level
    if player.ycor() >= player.finish_line:
        player.reset_position()
        score_board.update_level()
        cars.increasing_speed_of_cars()
    # detect collision with cars:
    for car in cars.cars_list:
        if player.distance(car) < 15:
            score_board.game_over()
            game_is_on = False


screen.exitonclick()
