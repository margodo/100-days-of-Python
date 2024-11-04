import turtle
from turtle import Turtle, Screen
from random import randint

colors = ["red","orange","yellow","green","blue","purple"]
myscreen = Screen()
myscreen.setup(500,400)
choice = myscreen.textinput("Make your bet",f"Which turtle will win the race? Enter a color: {colors}.")
print(choice)
y = [-100, -60, -20, 20, 60, 100]
turtles = []
is_race_on = False
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-240, y[i])
    turtles.append(new_turtle)

if choice:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        distance = randint(0,10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == choice:
               print(f"You have won! The {win_color} turtle is the winner! Congrats!")
            else:
                print(f"You have lost! The {win_color} turtle is the winner! Better luck next time!")


# def move():
#     timmy.forward(10)
# def backwards():
#     timmy.back(10)
# def counter_clock():
#     timmy.left(10)
# def clockwise():
#     timmy.right(10)
# def clear():
#     myscreen.resetscreen()
myscreen.listen()
# myscreen.onkey(key="w",fun=move)
# myscreen.onkey(key="s",fun=backwards)
# myscreen.onkey(key="a",fun=counter_clock)
# myscreen.onkey(key="d",fun=clockwise)
# myscreen.onkey(key="c",fun=clear)
myscreen.exitonclick()