# Summary of the Program Flow
![image](https://github.com/user-attachments/assets/beb57936-2e3b-466c-a300-b7832c70dbeb)

## Main Game Setup (`main.py`)
- Sets up the screen and creates instances of the `Snake`, `Food`, and `Scoreboard`.
- Listens for key inputs to control the snake's movement direction.
- Runs a game loop that updates the screen, moves the snake, checks for collisions, and updates the score or ends the game as necessary.

## Snake Behavior (`snake.py`)
- Initializes a three-segment snake and handles its movement, growth, and directional control.
- Contains logic to prevent reversing direction, ensuring smooth movement.

## Score Display (`scoreboard.py`)
- Displays the score at the top of the screen, updating it whenever the snake "eats" food.
- Displays a "Game Over" message when the game ends.

## Food Behavior (`food.py`)
- Creates a small red food item that randomly relocates each time it is "eaten" by the snake.
