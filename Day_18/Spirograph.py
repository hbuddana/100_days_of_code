import turtle as t
from turtle import Turtle, Screen
import random

bat = t.Turtle()
t.colormode(255)
bat.pensize(5)
bat.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        bat.color(random_color())
        bat.circle(100)
        bat.setheading(bat.heading()+ size_of_gap)


draw_spirograph(5)








screen = Screen()
screen.exitonclick()