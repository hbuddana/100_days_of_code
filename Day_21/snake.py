from turtle import Turtle

# Constants for initial snake setup and movement
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []          # List to store segments of the snake
        self.create_snake()         # Initialize the snake segments
        self.head = self.segments[0]# Head of the snake for easy reference

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)  # Adds each starting segment

    def add_segments(self, position):
        # Adds a single segment to the snake
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        # Adds a segment to the snake at the last segment's position
        self.add_segments(self.segments[-1].position())

    def move(self):
        # Move each segment to the position of the segment in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    # Direction control methods with checks to avoid reversing
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
