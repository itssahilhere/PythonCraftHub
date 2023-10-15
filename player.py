STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle,Screen
class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.penup()
    self.left(90)
    self.refresh()
  def move(self):
    self.forward(10) 
  def refresh(self):
    self.goto(STARTING_POSITION[0],STARTING_POSITION[1])   
  def finish(self):
    if(self.ycor()>250):
      return True
