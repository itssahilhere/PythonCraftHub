
from turtle import Turtle, Screen
import time
STRT_PNTS = [(0, 0), (-20, 0), (-40, 0)]
up = 90
down = 270
left = 180
right = 0
L = 20


class Snake:
    from turtle import Turtle, Screen
    import time

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in STRT_PNTS:
            self.add_segment(i)

            # add segment

    def add_segment(self, position):

        t = Turtle(shape='square')
        t.color('white')
        t.penup()
        t.goto(position)
        self.segment.append(t)

    def exten(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for i in range(len(self.segment)-1, 0, -1):
            x1 = self.segment[i-1].xcor()
            y1 = self.segment[i-1].ycor()
            self.segment[i].goto(x=x1, y=y1)
        self.segment[0].forward(L)

    def up(self):
        if(self.segment[0].heading() != down):
            self.segment[0].setheading(up)

    def down(self):
        if(self.segment[0].heading() != up):
            self.segment[0].setheading(down)

    def left(self):
        if(self.segment[0].heading() != right):
            self.segment[0].setheading(left)

    def right(self):
        if(self.segment[0].heading() != left):
            self.segment[0].setheading(right)
    def reset_snake(self):
        for i in self.segment:
            i.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]