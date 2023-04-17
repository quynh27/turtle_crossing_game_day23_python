from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.starting_position = STARTING_POSITION
        self.move_distance=MOVE_DISTANCE
        self.finish_line_y= FINISH_LINE_Y
        
    def move_up(self):
      
        self.forward(MOVE_DISTANCE)
        

        
