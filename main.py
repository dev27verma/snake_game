import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600,600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() > 295 or snake.head.ycor() < -300:
        game_is_on = False
        score.game_over()
        score.highest_score()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score.highest_score()
            score.game_over()

screen.exitonclick()