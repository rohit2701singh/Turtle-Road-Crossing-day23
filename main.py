from turtle import Turtle, Screen
from player import Player
from car import CarManager
from levelboard import Level
import time

screen = Screen()
screen.title("Turtle Road Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
level = Level()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()

    if player.ycor() > 290:
        player.reset_position()
        level.level_up()
        car_manager.increase_speed()

screen.exitonclick()
