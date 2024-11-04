import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.color("red")


#Draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon. With different colors
colors = ["Red", "Blue", "Orange", "Green"]
for i in range(3,10):
    tim.color(random.choice(colors))
    angle = 360/i

    for _ in range(i):
        tim.fd(100)
        tim.left(angle) 
        

"""
# Print a square using Turtle methods and a Loop
#for _ in range(4):
 #   tim.fd(100)
  #  tim.left(90)




# Print a Dashed Line using Turtle Methods and a Alternating Loop
for i in range(0,50):
    if i % 2 == 0:
        tim.pendown()
        tim.forward(10)
    else:
        tim.penup()
        tim.forward(10) 



Draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon. With different colors
colors = ["Red", "Blue", "Orange", "Green"]
for i in range(3,10):
    tim.color(random.choice(colors))
    angle = 360/i

    for _ in range(i):
        tim.fd(100)
        tim.left(angle) 
        



# Print a Random Walk with different colors

angle = [0,90,180,270]
colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan",
    "magenta", "violet", "indigo", "lime", "turquoise", "gold", "silver",
    "coral", "aqua", "lavender", "brown", "maroon", "teal", "olive"
]

turtle.speed(100)
turtle.pensize(10)

for _ in range(100):
    turtle.color(random.choice(colors))
    turtle.forward(50)
    turtle.left(random.choice(angle))

"""































screen = Screen()
screen.exitonclick()