from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        position_x = random.randint(-280, 280)
        position_y = random.randint(-280, 280)
        self.goto(position_x, position_y)

