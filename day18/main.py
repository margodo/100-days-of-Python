# Imports everything
# from turtle import *
# Imports as something
# import turtle as t
# timmy = t.Turtle()
import random
from random import choice
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("plum1")
t.colormode(255)
# for i in range (4):
#     tim.forward(100)
#     tim.right(90)
# for i in range(51):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
# # def draw_shape(num_sides):
# #     angle = 360 / num_sides
# #     for i in range (num_sides):
# #         tim.forward(100)
# #         tim.right(angle)
# #     tim.color(choice(colors))
# #
# # for num_sides in range(3,11):
# #     draw_shape(num_sides)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

# movements = [0,90,180,270]
# tim.pensize(12)
tim.speed("fastest")
# for i in range (150):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.seth(choice(movements))
def draw_spirograph(size):
    for i in range(0,360,size):
        tim.setheading(i)
        tim.color(random_color())
        tim.circle(100, None, 100)

draw_spirograph(5)





screen = t.Screen()
screen.exitonclick()