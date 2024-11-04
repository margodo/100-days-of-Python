from tkinter import *

from pandas import wide_to_long

window = Tk()

window.title("My first GUI program")
window.minsize(600,600)
# Label
my_label = Label(text = "I am a label", font=("Arial",24,"bold"))
my_label.pack()
my_label["text"] = "new text"
my_label.config(text="Hi")

def button_click():
    my_label["text"] = user_input.get()

button = Button(text="click me", command=button_click)
button.pack()

#Entry
user_input = Entry(width=10)
user_input.insert(END, string = "type here")
print(user_input.get())
user_input.pack()

#Text
text = Text(height=5, width=15)
text.focus()
text.insert(END,"Example. Hello there. My name is Alex\n")
#Gets current value in text box at line 1, character 0
print(text.get("1.0", END))
text.pack()

def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_= 0, to = 10, width = 5, command=spinbox_used)
spinbox.pack()

def scale_used(value):
    print(value)

scale = Scale(from_=0, to = 100, command=scale_used)
scale.pack()

def checkbutton_use():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state,command=checkbutton_use)
checked_state.get()
checkbutton.pack()

def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1,variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2,variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


def listbox_used(event):
    print((listbox.get(listbox.curselection())))
listbox = Listbox(height=4)
fruits = ["Apple","Pear","Orange","Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()

window.mainloop()