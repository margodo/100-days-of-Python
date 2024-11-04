from tkinter import *

def button_click():
    km_output.config(text = round(float(user_input.get())*1.60934,2))

#Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(200,100)
window.config(padx=20,pady=20)

user_input = Entry(width=10)
user_input.grid(column = 1, row = 0)

miles = Label(text="Miles")
miles.grid(column = 2, row = 0)
output_text = Label(text="is equal to")
output_text.grid(column = 0,row =1)
km_output = Label(text = "0")
km_output.grid(column = 1, row = 1)
km = Label(text="Km")
km.grid(column = 2, row = 1)

button_calculate = Button(text="Calculate", command=button_click)
button_calculate.grid(column = 1, row = 2)

window.mainloop()