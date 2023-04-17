from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        
        self.hideturtle()
        self.penup()
        
        self.level =0
        self.write_board()
        
    
    def write_board(self):
        
        self.pencolor('black')
        self.goto(x=-200,y=250)
        
        self.write(f'Level: {self.level}',False,'center',FONT)
        
    def increase_level(self):
        self.level +=1

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER',False,'center',FONT)
       

        
          
    
