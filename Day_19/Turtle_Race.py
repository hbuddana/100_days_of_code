from turtle import Turtle, Screen
import random

# Create the screen
screen = Screen()
screen.setup(width=500, height=400)

# Prompt user for their bet
user_bet = screen.textinput("Make Your bet", "Which turtle will win the race? Enter a color: ")

# Define the colors and starting positions
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []  # List to store turtle instances

# Initial x and y positions
x_ip = -230
y_ip = -100

# Create a turtle for each color
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()  # Make sure the turtle doesn't draw a line while moving
    new_turtle.goto(x=x_ip, y=y_ip)
    turtles.append(new_turtle)  # Store the turtle instance in the list
    y_ip += 50  # Move the next turtle up by 50 units to align them in a row

# Start the race
is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        # Move each turtle a random distance between 0 and 10
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        # Check if a turtle has crossed the finish line (x=230)
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations! You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry, you've lost. The {winning_color} turtle won the race.")
            break
# Keep the screen open until clicked
screen.exitonclick()
