from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

SPACING = -20

snake_body_segments = []
game_is_on = True

for body_segment_index in range(3):
    new_body_segment = Turtle(shape='square')
    new_body_segment.color('white')
    x = body_segment_index * SPACING
    new_body_segment.penup()
    new_body_segment.setx(x)
    snake_body_segments.append(new_body_segment)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(snake_body_segments) - 1, 0, -1):
        new_x = snake_body_segments[seg_num - 1].xcor()
        new_y = snake_body_segments[seg_num - 1].ycor()
        snake_body_segments[seg_num].setposition(new_x, new_y)
    snake_body_segments[0].forward(20)
    snake_body_segments[0].left(90)

screen.exitonclick()


