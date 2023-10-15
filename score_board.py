FONT = ("Courier", 24, "normal")
from turtle import Turtle,Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.levl=1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280,250)
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Courier",50,"normal"))
    def update(self):
        self.clear()
        self.write(f"LEVEL :{self.levl}",align="left",font=("Courier",20,"normal"))
    def level(self):
        self.levl=self.levl+1
        self.update()



   
