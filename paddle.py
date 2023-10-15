from turtle import Turtle,Screen
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
    def create(self,d):
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(d[0],d[1])
    def go_up(self):
        y_co=self.ycor()+20
        self.goto(self.xcor(),y_co)
    def go_down(self):

         y_co=self.ycor()-20
         self.goto(self.xcor(),y_co)
