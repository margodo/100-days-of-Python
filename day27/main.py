from tkinter import *


def button_click():
    my_label["text"] = user_input.get()

#Window
window = Tk()
window.title("My first GUI program")
window.minsize(600,600)
window.config(padx=20,pady=20)

# Label
my_label = Label(text = "I am a label", font=("Arial",24,"bold"))
my_label["text"] = "new text"
my_label.config(text="Hi")
my_label.grid(column=0,row=0)
my_label.config(padx=10,pady=10)

#Button
button = Button(text="click me", command=button_click)
button.grid(column = 1,row = 1)
button2 = Button(text="no, click me", command=button_click)
button2.grid(column = 2,row = 0)

#Entry
user_input = Entry(width=10)
user_input.insert(END, string = "type here")
print(user_input.get())
user_input.grid(column=3,row= 3)



window.mainloop()