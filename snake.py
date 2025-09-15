from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    snake_body_segments = []

    def __init__(self):
        self.create_snake()
        self.head = self.snake_body_segments[0]

    def create_snake(self):
        """Create the initial snake body.

        The snake starts with three white square turtle segments,
        each positioned -20 units apart along the x-axis.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        """Create a new white square segment at the given position and add it to the snake body."""
        new_body_segment = Turtle(shape='square')
        new_body_segment.color('white')
        new_body_segment.penup()
        new_body_segment.goto(position)
        self.snake_body_segments.append(new_body_segment)

    def extend(self):
        """Extend the snake by adding a new segment at its tail."""
        self.add_segment(self.snake_body_segments[-1].pos())

    def move(self):
        """Move the snake forward by one step.

        Each segment takes the position of the segment ahead of it,
        and finally the head moves forward by 20 units.
        """
        for seg_num in range(len(self.snake_body_segments) - 1, 0, -1):
            new_x = self.snake_body_segments[seg_num - 1].xcor()
            new_y = self.snake_body_segments[seg_num - 1].ycor()
            self.snake_body_segments[seg_num].setposition(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turn the snake upward, unless it is currently facing down. """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        """Turn the snake right, unless it is currently facing left. """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Turn the snake left, unless it is currently facing right. """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        """Turn the snake downward, unless it is currently facing up. """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

