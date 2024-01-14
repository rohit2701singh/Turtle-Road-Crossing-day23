from turtle import Turtle
import random

STARTING_MOVING_DISTANCE = 5
MOVE_INCREMENT = 10

CAR_COLORS = ["RoyalBlue", "red", "blue", "green", "pink", "yellow", "brown", "DeepSkyBlue", "DimGray", "MidnightBlue",
              "Lime", "DarkOrange", "Sienna", "DarkViolet", "LightCoral", "Olive"]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVING_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)    # this will reduce car generation speed.
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.speed = STARTING_MOVING_DISTANCE
            new_car.color(random.choice(CAR_COLORS))
            new_car.shapesize(stretch_wid=0.8, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-260, 280)
            new_car.goto(300, random_y)    # send all cars from center to right edge (x=300) of screen
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVING_DISTANCE)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
