from turtle import  Turtle

FONT = ('Arial', 16, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.the_highest_score = 0
        self.color("gold")
        self.penup()
        self.goto(x = -150, y = 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("score_history.txt", mode="r") as file:
            score_history = file.read()
        self.write(arg=f"Current score: {self.score}   VS   The highest score: {score_history}", move=False, font=FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.the_highest_score:
            self.the_highest_score = self.score
            with open("score_history.txt", mode="w") as file:
                file.write(f"{self.the_highest_score}")
        self.score = 0
        self.update_scoreboard()

