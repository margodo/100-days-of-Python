class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q. {self.question_number}: {current_question.text} True or False?\n')
        self.check_answer(user_answer, current_question.answer)
        return user_answer

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer.title() == question_answer:
            self.score += 1
            print('You fot it right!')
        else:
            print('This is wrong.')
        print(f'The actual answer is {question_answer}')
        print(f'Your score is: {self.score} / {self.question_number}')
        print('\n')
