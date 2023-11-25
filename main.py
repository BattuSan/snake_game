from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.tracer(0)
screen.bgcolor('black')

python_box = []
position = 0
for _ in range(3):
    turtle = Turtle()
    turtle.shape("square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(position, 0)
    position -= 20
    python_box.append(turtle)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(python_box)-1, 0, -1):
        new_x = python_box[i-1].xcor()
        new_y = python_box[i-1].ycor()
        python_box[i].goto(new_x, new_y)
    python_box[0].forward(20)
screen.exitonclick()
