import math
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    check_mark.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        count_down(short_break)
        timer_label.config(text = "Break", fg = PINK)
    elif REPS % 2 == 0:
        count_down(long_break)
        timer_label.config(text = "Break", fg = RED)
    else:
        count_down(work_sec)
        timer_label.config(text = "Work", fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds <= 9:
        seconds = f'0{seconds}'
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down,count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✓"
        check_mark.config(text = mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg = YELLOW)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME,40,"bold"), bg=YELLOW)
timer_label.grid(column = 1, row = 0)

canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image = tomato)
timer_text = canvas.create_text(100,132, text = "00:00",fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row =1)

start_button = Button(text="Start", highlightthickness=0, font = (FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column = 0, row = 2)
reset_button = Button(text="Reset", highlightthickness=0, font = (FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(column = 2, row = 2)

check_mark = Label(fg=GREEN, font=(FONT_NAME,20,"normal"), bg=YELLOW)
check_mark.grid(column = 1, row = 3)

window.mainloop()