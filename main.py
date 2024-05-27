from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(fun=player.go_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with turtle
    for car in car_manager.all_cars:
       if car.distance(player) < 20:
           game_is_on = False
           level.game_over()

    #Detect if turtle reaches the other side
    if player.ycor() > 280:
        player.finish_line()
        car_manager.increase_speed()
        level.update_level()


