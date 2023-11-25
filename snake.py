from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake_box = []
        self.position = 0
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            turtle = Turtle()
            turtle.shape("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(self.position, 0)
            self.position -= 20
            self.snake_box.append(turtle)

    def move(self):
        for i in range(len(self.snake_box)-1, 0, -1):
            new_x = self.snake_box[i-1].xcor()
            new_y = self.snake_box[i-1].ycor()
            self.snake_box[i].goto(new_x, new_y)
        self.snake_box[0].forward(20)

    def up(self):
        self.snake_box[0].setheading(90)

    def down(self):
        self.snake_box[0].setheading(270)

    def left(self):
        self.snake_box[0].setheading(180)

    def right(self):
        self.snake_box[0].setheading(0)
