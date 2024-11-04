from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words = []
#--------------------Change text of the card---------------------------#
def change_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(words)
    canvas.itemconfig(canvas_image,image=front)
    canvas.itemconfig(language,text = "French",fill="black")
    canvas.itemconfig(word_on_card,text = current_card["French"],fill="black")
    timer = window.after(3000,flip_card)

#-------------------Flip card--------------------------------------------#
def flip_card():
    global current_card
    canvas.itemconfig(language,text="English",fill = "white")
    canvas.itemconfig(canvas_image,image = back)
    canvas.itemconfig(word_on_card,text = current_card["English"],fill="white")
#----------------------Remove known card-----------------------------#
def is_known():
    words.remove(current_card)
    data = pandas.DataFrame(words)
    data.to_csv("./data/words_to_learn.csv",index=False)
    change_card()
#---------------------------------UI--------------------------------#
window = Tk()
window.config(bg=BACKGROUND_COLOR,pady=50,padx=50)
window.title("Flashy")
timer = window.after(3000,flip_card)
# Images
front = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="./images/card_back.png")
cross_image = PhotoImage(file="./images/wrong.png")
tick_image = PhotoImage(file="./images/right.png")

#Convert csv
try:
    words_file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = words_file.to_dict(orient="records")

#canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_image = canvas.create_image(400,263, image=front)
canvas.grid(row=0,column=0, columnspan = 2)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_on_card = canvas.create_text(400,263, text = "", font=("Arial", 60, "bold"))

button_right = Button(image=tick_image, highlightthickness=0, command=is_known)
button_right.grid(row =1, column = 1)
button_wrong = Button(image=cross_image, highlightthickness=0,command=change_card)
button_wrong.grid(row=1,column=0)

change_card()






















window.mainloop()
