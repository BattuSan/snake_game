from turtle import Turtle, Screen
import time

import scoreboard
from snake import Snake
import food

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.tracer(0)
screen.bgcolor('black')

food = food.Food()
score_game = scoreboard.Scores()
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        # random food placement
        food.refresh()
        # score_board
        score_game.score += 1
        score_game.display_score()
        print(snake.head.xcor())
        print(snake.head.ycor)
        # wall collision detection
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_game.game_over()
        game_is_on = False


screen.exitonclick()
