from turtle import Turtle,Screen
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("white")
        self.penup()
        self.mov=10
        self.mov1=10
        self.s=0.1
    def move_X(self):
        x=self.xcor()+self.mov
        y=self.ycor()+self.mov1
        self.goto(x,y)
    def bounce(self):
        self.mov1*=-1
    def bounce1(self):
        self.mov*=-1
        self.s*=0.9
        
