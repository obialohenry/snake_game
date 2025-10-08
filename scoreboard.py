from turtle import Turtle
STARTING_Y = 270
ALIGNMENT ="center"
FONT=("Arial",22,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.sety(STARTING_Y)
        self.score = 0
        try:
            with open("data.txt") as data:
             self.high_score = int(data.read())
        except ValueError:
            self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear previous score from screen, and writes current score on screen."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,font=FONT)
    
    def reset(self):
        """Reset the scoreboard.

           If the current score is greater than the high score, update the high score.
           Then reset the current score to 0 and refresh the display.
        """
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increase current score by 1 after the snake have eaten food, and updates the score board."""
        self.score +=1
        self.save_high_score_locally()
        self.update_scoreboard()

    def save_high_score_locally(self):
     """Save the player's high score.

        If the current score is greater than the high score, update the high score.
        Then save in the device storage, by writing the new highscore in a local text file(data.txt).
     """
     if self.score > self.high_score:
        self.high_score = self.score
        with open("data.txt", mode='w') as data:
            data.write(f"{self.high_score}")
