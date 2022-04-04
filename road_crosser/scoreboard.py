from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(x=-280, y=270)
        self.write(f"Level: {self.score}", font=("Arial", 20, "normal"))

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over", font=("Arial", 30, "normal"), align="center")