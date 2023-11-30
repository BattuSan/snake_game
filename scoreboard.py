from turtle import Turtle


class Scores(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 30, "normal"))
