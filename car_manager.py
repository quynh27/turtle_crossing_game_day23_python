from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self) -> None:
        
        self.cars =[]
        self.move_speed = STARTING_MOVE_DISTANCE 
        
        for color in COLORS:
            
            self.create_car() 
    
         


    def create_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.shapesize(stretch_len=2,stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.penup()
         
        new_car.goto(x= 260,y=random.randint(-250,250))
        new_car.setheading(180)
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        self.cars.append(new_car)

        
                

    def move(self):
        for car in self.cars:
            if car.xcor() > -260:
                
                car.forward(self.move_speed)
            else:
                car.goto(x= 260,y=random.randint(-250,250))
                car.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT



