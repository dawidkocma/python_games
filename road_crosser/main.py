from turtle import Screen
from scoreboard import Score
from cars import Car
import time
from player import Player
screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

player = Player()
scoreboard = Score()
car_manager = Car()
screen.listen()
screen.onkey(player.go_up, "Up")
game_on = True

while game_on:

    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    #Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    #Detect finish line
    if player.ycor() > 280:
        scoreboard.update_scoreboard()
        player.start_position()
        car_manager.level_up()

screen.exitonclick()