from turtle import Turtle

FONT = ('Arial', 16, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.color("red")
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-20, y=280)
        self.write(arg=f"LEVEL: {self.level}", align="center", move=False, font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(arg="CRASH! GAME OVER!", align="center", move=False, font=FONT)

