from turtle import Turtle

START = (0, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10

    def create_ball(self):
        self.penup()
        self.shape("circle")
        self.color('red')
        self.shapesize(1, 1)

    def ball_move(self):
        # for i in range(0,10):
        # self.clear()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        print(f"{new_x},{new_y}")
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
