# TODO Screen
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
# TODO Scoreboard

# TODO Players
ball = Ball()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
score = Scoreboard()

game_on = True
while game_on:
    screen.update()
    score.update_score("default")
    time.sleep(ball.move_speed)
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
# TODO ball
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
# TODO screen splitter
    if ball.xcor() > 390:
        ball.reset_position()
        score.update_score("player_l")
    if ball.xcor() < -390:
        ball.reset_position()
        score.update_score("player_r")



screen.exitonclick()
