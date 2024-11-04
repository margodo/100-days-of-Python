THEME_COLOR = "#375362"
FONT = ("Arial",18,"italic")

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas = Canvas(width=300,height=250,highlightthickness=0)
        self.canvas.grid(row=1,column=0,columnspan = 2,sticky="EW",pady=50)
        self.queston_text = self.canvas.create_text(150,125,text="Welcome",font=FONT,fill=THEME_COLOR,width=250)
        self.score_label = Label(text=f"Score: {self.quiz.score}",fg="white",bg=THEME_COLOR, font=("Arial",12,"normal"))
        self.score_label.grid(row=0,column=1)
        tick_image = PhotoImage(file="./images/true.png")
        cross_image = PhotoImage(file="./images/false.png")

        self.tick_button = Button(image=tick_image, highlightthickness=0,command=self.true_answer)
        self.tick_button.grid(row = 2,column=0)
        self.cross_button = Button(image = cross_image, highlightthickness=0,command = self.false_answer)
        self.cross_button.grid(row = 2,column =1)

        self.get_next_q()
        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.queston_text,text = q_text)
        else:
            self.canvas.itemconfig(self.queston_text,text="You have finished the quiz. Thank you for playing!")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("true")
        self.feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer("false")
        self.feedback(is_right)

    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1500,self.get_next_q)

