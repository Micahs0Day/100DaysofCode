from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions() is True:
    quiz_brain.next_question()

q_num = quiz_brain.question_number
u_score = quiz_brain.user_score
print("You've completed the quiz!!!")
print(f"Your final score is: {u_score}/{q_num} ")

