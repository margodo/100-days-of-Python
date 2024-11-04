from question_model import Question
from data import question_data
import quiz_brain
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

score = 0
game_over = True
while quiz.still_has_question():
    quiz.next_question()

print(f'You have completed the quiz.\nYour final score is {quiz.score}/{quiz.question_number}')