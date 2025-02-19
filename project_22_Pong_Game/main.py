from turtle import Screen
from paddle import Paddle
from ball import Ball
import  time
from score_board import  ScoreBoard

screen = Screen()
screen.setup(width=800, height=600, startx=0, starty=0)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.speed_set)
    ball.move()
    #detect collision with top of the wall --> bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with right paddle - bounce
    if ball.distance(right_paddle) < 50 and  ball.xcor() > 320:
        ball.bounce_x()
    # detect collision with left paddle --> bounce
    if ball.distance(left_paddle) < 50 and  ball.xcor() <- 320:
        ball.bounce_x()
    # detect when right paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.increase_score_left_player()
    # detect when left paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.increase_score_right_player()

screen.exitonclick()
