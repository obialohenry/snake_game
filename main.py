from turtle import Screen, Turtle

SPACING = -20

for turtle_index in range(3):
    print(turtle_index)
    new_turtle = Turtle(shape='square')
    new_turtle.color('white')
    x = turtle_index * SPACING
    new_turtle.setx(x)

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')

screen.exitonclick()


