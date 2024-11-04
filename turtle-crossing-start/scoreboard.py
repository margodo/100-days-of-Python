FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 250)
        self.showlevel()

    def showlevel(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center", FONT)


