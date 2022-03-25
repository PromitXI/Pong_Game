from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('lime')
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0

        self.update_scoreboard()






    def update_scoreboard(self):
        self.goto(100, 200)
        self.write(self.r_score, font=('Courier', 80, 'bold'), align='left')
        self.goto(-100, 200)
        self.write(self.l_score, font=('Courier', 80, 'bold'), align='left')
    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()


    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
