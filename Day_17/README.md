## Project Overview

### Quiz Game Project

This project is a **True/False Quiz Game** implemented in Python. It allows users to answer questions, tracks their score, and displays the final result at the end of the game. Here is a breakdown of the key components:

---

#### Data Source (`data.py`)

- The questions are stored in a list format, with each question being a dictionary containing `text` (the question) and `answer` (the correct answer: True or False).

---

#### Question Model (`question_model.py`)

- The `Question` class defines a question object that encapsulates the question's text and the correct answer. This abstraction allows for easy manipulation and access to question data.

---

#### Quiz Logic (`quiz_brain.py`)

- The `QuizBrain` class controls the quiz's progression:
  - It keeps track of the current question number and the user's score.
  - It has a method `still_has_questions()` to check if there are more questions.
  - The `next_question()` method prompts the user with the next question and uses `check_answer()` to verify the answer and update the score.

---

#### Main Program (`main.py`)

- This file initializes the quiz by converting question data into `Question` objects and loading them into the `QuizBrain` instance.
- The main loop then runs, prompting the user with questions until the quiz is complete, at which point the final score is displayed.

---
