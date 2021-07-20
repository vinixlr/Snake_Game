from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.score_update()


    def score_update(self):
        self.write(arg=f"Score: {self.score} ", align="center", font=("Arial,", 18, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial,", 18, "normal"))

    def score_increase(self):
        self.clear()
        self.score += 1
        self.score_update()

