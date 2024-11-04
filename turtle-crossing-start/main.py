import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
carmanager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.up,"Up")

game_is_on = True

while game_is_on:
    carmanager.create_car()
    time.sleep(0.1)
    screen.update()
    carmanager.move()
    for car in carmanager.cars:
        if car.distance(player) < 25:
            score_board.game_over()
            game_is_on = False
    if player.succesful_crossing():
        score_board.level += 1
        score_board.showlevel()
        carmanager.level_up()
        player.go_to_start()

screen.exitonclick()