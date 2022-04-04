from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(x=0, y=260)
        self.score_l = 0
        self.score_r = 0
        self.write(f"{self.score_l} : {self.score_r}", False, align="center", font=("Arial", 20, "normal"))

    def update_score(self, player):
        if player == "player_l":
            self.score_l += 1
            self.clear()
            self.write(f"{self.score_l} : {self.score_r}", False, align="center", font=("Arial", 20, "normal"))
        elif player == "player_r":
            self.score_r += 1
            self.clear()
            self.write(f"{self.score_l} : {self.score_r}", False, align="center", font=("Arial", 20, "normal"))
        else:
            self.clear()
            self.write(f"{self.score_l} : {self.score_r}", False, align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 25, "normal"))
