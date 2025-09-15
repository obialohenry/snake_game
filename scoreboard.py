from turtle import Turtle
STARTING_Y = 280
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.sety(STARTING_Y)
        self.score = 0
        self.write(f"Score: {self.score}",align='center')

    def increase_score(self):
        """Increase current score by 1 after the snake have eaten food."""
        self.clear()
        self.score = self.score +1
        self.write(f"Score: {self.score}", align='center')