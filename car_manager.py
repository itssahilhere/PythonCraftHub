COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle,Screen
class CarManager():
    def __init__(self):
        self.all=[]
        self.speed=STARTING_MOVE_DISTANCE
    def create(self):
        import random
        te=random.randint(1,6)
        if(te==6):
            t=Turtle("square")
            t.shapesize(1,2)
            t.color(random.choice(COLORS))
            t.penup()
            y=random.randint(-250,250)
            t.goto(300,y)
            self.all.append(t)  
    def move(self):
        for i in self.all:
            i.backward(self.speed)
    def level_up(self):
        self.speed+=MOVE_INCREMENT
