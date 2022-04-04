# TODO: Create snake
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jake the snake")
#turn off the animation
screen.tracer(0)
position = 20
snake_length = []


snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO: detect collision
    if snake.head.distance(food) < 15:
        score.update_score()
        snake.extend()
        food.refresh()

    #Detect wall collision
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on = False
        score.game_over()

    #Detect head collision with any of the segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()



# TODO: Detect collision with tail
