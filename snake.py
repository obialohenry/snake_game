from turtle import Turtle
SPACING = -20
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
        each spaced -20 units apart along the x-axis.
        """
        for body_segment_index in range(3):
            new_body_segment = Turtle(shape='square')
            new_body_segment.color('white')
            x = body_segment_index * SPACING
            new_body_segment.penup()
            new_body_segment.setx(x)
            self.snake_body_segments.append(new_body_segment)

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

