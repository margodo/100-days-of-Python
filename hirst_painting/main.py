# import turtle as t
# import random
# from turtle import Turtle, Screen
#
# from PIL.ImImagePlugin import number
#
# # import colorgram
# # rgb_colors = []
# # colors = colorgram.extract('image.jpg', 7)
# # for color in colors:
# #     r = color.rgb.r
# #     g = color.rgb.g
# #     b = color.rgb.b
# #     new_color = (r,g,b)
# #     rgb_colors.append(new_color)
# # print(rgb_colors)
# t.colormode(255)
# rgb_colors = [(251, 243, 248), (242, 250, 246), (233, 223, 85), (189, 10, 67), (112, 178, 211)]
#
# tim = Turtle()
# screen = Screen()
# tim.hideturtle()
# tim.penup()
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# # def draw_row():
# #     tim.penup()
# #     for i in range(10):
# #         color = random.choice(rgb_colors)
# #         tim.dot(20, color)
# #         tim.forward(50)
# #
# # def change_row():
# #     tim.penup()
# #     tim.back(500)
# #     tim.left(90)
# #     tim.forward(30)
# #     tim.right(90)
# #
# # for i in range(10):
# #     draw_row()
# #     change_row()
# number_of_dots = 100
# for dot_count in range(1,number_of_dots + 1):
#     tim.dot(20,random.choice(rgb_colors))
#     tim.forward(50)
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
# screen.exitonclick()

import turtle as t
import random

color_list = [(36, 95, 183), (236, 165, 79), (244, 223, 87), (215, 69, 105), (98, 197, 234), (250, 51, 22),
              (203, 70, 21), (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166), (165, 175, 233),
              (66, 45, 13), (72, 205, 170), (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0), (164, 28, 8),
              (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98), (98, 96, 186)]
timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()
# timmy is hidden to increase drawing speed
for i in range(10):
    timmy.setposition(-250, -250 + 50 * i)
    for _ in range(10):
        new_color = random.choice(color_list)
        timmy.color(new_color)
        timmy.begin_fill()
        timmy.circle(10)
        timmy.end_fill()
        timmy.forward(50)

screen = t.Screen()
screen.exitonclick()