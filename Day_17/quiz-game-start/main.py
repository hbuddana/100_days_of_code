# Import necessary classes and data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Initialize an empty question bank list
question_bank = []

# Populate question_bank with Question objects created from question_data
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize QuizBrain with the question bank
quiz = QuizBrain(question_bank)

# Start the quiz loop
while quiz.still_has_questions():
    quiz.next_question()

# Print the final score after the quiz completes

print("You have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
