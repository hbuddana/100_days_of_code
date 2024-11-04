# Importing the Turtle and Screen classes from the turtle module
from turtle import Turtle, Screen

# Create a Turtle object named 'tim'
tim = Turtle()

# Create a Screen object to handle the turtle graphics window
screen = Screen()

# Set the screen to listen for key presses
screen.listen()

# Function to move the turtle forwards by 30 units
def move_forwards():
    tim.forward(30)

# Function to move the turtle backwards by 30 units
def move_backwards():
    tim.bk(30)

# Function to rotate the turtle counterclockwise by 180 degrees
def move_cclock():
    tim.left(180)

# Function to rotate the turtle clockwise by 180 degrees
def move_clock():
    tim.right(180)

# Function to clear the canvas and reset the screen
def clean_canvas():
    screen.reset()

# Binding the 'w' key to move the turtle forwards
screen.onkey(key="w", fun=move_forwards)

# Binding the 's' key to move the turtle backwards
screen.onkey(key="s", fun=move_backwards)

# Binding the 'a' key to rotate the turtle counterclockwise
screen.onkey(key="a", fun=move_cclock)

# Binding the 'd' key to rotate the turtle clockwise
screen.onkey(key="d", fun=move_clock)

# Binding the 'c' key to clear the canvas and reset the screen
screen.onkey(key="c", fun=clean_canvas)

# Wait for the user to click on the screen to exit the program
screen.exitonclick()
