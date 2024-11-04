from player import STARTING_POSITION

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1 or random_chance == 2:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250,250))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
