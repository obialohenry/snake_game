from turtle import Turtle
import random as r

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color('red')
        self.speed(0)
        self.refresh()

    def refresh(self):
        """Set the food to a random x and y coordinate on the screen."""
        random_x = r.randint(-280, 280)
        random_y = r.randint(-280, 280)
        self.goto(random_x, random_y)
