from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Metallic", 16,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0,260)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. Highest score: {self.high_score}", False, ALIGNMENT,FONT)
    def reset_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()