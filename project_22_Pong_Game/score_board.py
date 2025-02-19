from turtle import  Turtle

FONT = ('Arial', 64, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.score_right_player = 0
        self.score_left_player = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=-100, y=200)
        self.write(arg=self.score_left_player, align="center", move=False, font=FONT)
        self.goto(x=100, y=200)
        self.write(arg=self.score_right_player, align="center", move=False, font=FONT)

    def increase_score_left_player(self):
        self.clear()
        self.score_left_player += 1
        self.update_scoreboard()

    def increase_score_right_player(self):
        self.clear()
        self.score_right_player += 1
        self.update_scoreboard()
