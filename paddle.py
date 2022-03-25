from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.position = pos

        self.create_paddle(position=pos)

    def create_paddle(self, position):
        self.penup()
        self.shape('square')
        self.color('white')

        self.shapesize(5, 1)
        self.goto(position)

    def paddle_up(self):
        new_y = (self.ycor() + 50)
        self.goto(x=self.xcor(), y=new_y)

    def paddle_down(self):
        new_y = (self.ycor() - 50)
        self.goto(self.xcor(), new_y)
