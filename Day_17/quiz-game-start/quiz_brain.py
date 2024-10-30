# QuizBrain manages the quiz flow, questions, and score
class QuizBrain:
    # Initialize with a list of questions, starting score and question number
    def __init__(self, q_list):
        self.question_number = 0  # Current question index
        self.score = 0  # User score
        self.question_list = q_list  # List of question objects

    # Check if there are more questions in the list
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Ask the next question and check the user's answer
    def next_question(self):
        current_question = self.question_list[self.question_number]  # Current question object
        self.question_number += 1  # Increment question count
        # Prompt user for an answer and pass it to check_answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    # Compare user's answer to the correct answer
    def check_answer(self, user_answer, correct_answer):
        # If the answer is correct, update the score
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's Wrong")

        # Display current score
        print(f"Your Current score is {self.score} / {self.question_number}")
