class QuizBrain:
    

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}: {current_question.text} (True\False):")
        self.check_ansewr(user_answer, current_question.answer)

    def check_ansewr(self, user_answer, correct_answer):
        score = 0
        if user_answer.lower() == correct_answer.lower():
            score += 1
            print("You got it right")
        else:
            print("That's a wrong. ")
        print(f"The correct answer was: {correct_answer}.")
