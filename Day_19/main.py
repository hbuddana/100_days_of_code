from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.fd(10)


screen.listen()
screen.onkey(key="space", fun = move_forwards) # Higher Order fn's

screen.exitonclick()