from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off automatic screen updates for smooth animation

# Create instances of Snake, Food, and Scoreboard classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Setting up key listeners to control snake direction
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()        # Manually updates the screen for smooth animation
    time.sleep(0.1)        # Adds a delay for controlling game speed
    snake.move()           # Moves the snake forward

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()        # Move food to a new random location
        snake.extend()             # Add a new segment to the snake
        scoreboard.increase_score()# Update the score

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()     # Display "Game Over" when the snake hits the wall

    # Detect collision with itself
    for segment in snake.segments[1:]:  # Check each segment after the head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()     # Display "Game Over" when snake collides with itself

screen.exitonclick()  # Keep screen open until user clicks
