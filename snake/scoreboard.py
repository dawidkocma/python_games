from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(x=0, y=260)
        self.score = 0
        self.write(f"Score: {self.score} ", False, align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", False, align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=("Arial", 25, "normal"))
