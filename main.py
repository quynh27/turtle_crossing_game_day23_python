import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
cars= CarManager()
screen.listen()

screen.onkey(fun=turtle.move_up,key='Up')

scoreboard = Scoreboard()
game_is_on = True
counter =0
while game_is_on:
    counter +=1
    time.sleep(0.1)
    if counter % 6 == 0:
        cars.create_car()
    cars.move()

    if turtle.ycor() > turtle.finish_line_y -20:
        scoreboard.increase_level()
        scoreboard.clear()
        scoreboard.write_board()
        turtle.goto(turtle.starting_position)
        cars.increase_speed()      
    else:
       
        for car in cars.cars:
            if turtle.distance(car) <20:
                scoreboard.game_over()
                game_is_on= False
                break
   

    screen.update()

   
    

screen.exitonclick()