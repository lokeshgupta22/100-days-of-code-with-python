class QuizBrain:
    def __init__(self, questionbank):
        self.question_number = 0
        self.question_list = questionbank
        self.score = 0

    '''def still_has_question(self):
        if self.question_number >= len(self.question_list):
            return False
        return True'''

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(
            f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(ans, question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
