from turtle import Turtle
STARTING_Y = 280
ALIGNMENT ="center"
FONT_FAMILY = "Arial"
FONT_SIZE = 24
FONT_TYPE = "normal"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.sety(STARTING_Y)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear previous score from screen, and writes current score on screen."""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT,font=(FONT_FAMILY,FONT_SIZE,FONT_TYPE))

    def increase_score(self):
        """Increase current score by 1 after the snake have eaten food, and updates the score board."""
        self.score +=1
        self.update_scoreboard()