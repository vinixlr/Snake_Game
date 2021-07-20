from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("VINICIUS Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.update()

snake = Snake()
food = Food()
board_score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_in_on = True

while game_in_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        board_score.score_increase()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or \
            snake.segments[0].ycor() < -280:
        board_score.game_over()
        game_in_on = False

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 5:
            game_in_on = False
            board_score.game_over()


screen.exitonclick()
