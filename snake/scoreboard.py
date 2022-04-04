from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(x=0, y=260)
        self.score = 0
        with open("data.txt") as file:
            read_score = file.read()
            self.high_score = int(read_score)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
