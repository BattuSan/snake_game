from turtle import Turtle

MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_box = []
        self.position = 0
        self.create_snake()
        self.head = self.snake_box[0]

    def create_snake(self):
        for _ in range(3):
            turtle = Turtle()
            turtle.shape("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(self.position, 0)
            self.position -= MOVE
            self.snake_box.append(turtle)

    def move(self):
        for i in range(len(self.snake_box) - 1, 0, -1):
            new_x = self.snake_box[i - 1].xcor()
            new_y = self.snake_box[i - 1].ycor()
            self.snake_box[i].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
