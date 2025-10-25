from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)

while quiz.still_ques():
    quiz.next_ques()

print("You've completed the quiz!")
print(f"Your final score: {quiz.score}/{quiz.question_number}")
