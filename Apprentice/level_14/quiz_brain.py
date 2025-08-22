class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?:"
        ).lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}")
        print(f"Your current score  is:{self.score}/{self.question_number}")
        print("\n")

    def quiz_ended(self):
        print("You've completed the quiz")
        print(f"Your final score was:{self.score}/{self.question_number}")
