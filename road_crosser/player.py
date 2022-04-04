from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.start_position()

    def start_position(self):
        self.setheading(90)
        self.setposition(x=0, y=-270)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

