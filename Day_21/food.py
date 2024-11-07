from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")                    # Shape of the food
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Resize food to half size
        self.color("red")                       # Color of the food
        self.speed("fastest")                   # Speed up food's appearance
        self.refresh_food()                     # Initialize food in a random location

    def refresh_food(self):
        # Move the food to a random position on the screen
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
