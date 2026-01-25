from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    q_text = data["text"]
    q_answer = data["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You completed the quiz")
print(f"You final score was: {quiz.score}/ {quiz.question_number}")
