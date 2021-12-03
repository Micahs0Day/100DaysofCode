class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.user_score = 0

    def still_has_questions(self):
        q_length = len(self.question_list)
        if self.question_number == q_length:
            return False
        else:
            return True

    def next_question(self):
        q_text = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {q_text.text} (True/False)?: ").lower()
        self.check_answer(user_answer, q_text.answer)
        print(f"Your current score is: {self.user_score}/{self.question_number}\n")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.user_score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}")

