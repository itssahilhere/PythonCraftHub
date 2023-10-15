from turtle import Turtle,Screen, TurtleScreen, width
from paddle import Paddle
from ball import Ball
from sc import Score
import time
t=Screen()
s=Turtle()
score=Score()
t.setup(width=800,height=600)
s.speed("fast")
t.bgcolor("black")
t.title("PONG GAME")
t.tracer(0)
p1=Paddle()
p2=Paddle()
b=Ball()
p1.create((350,0))
p2.create((-350,0))
t.listen()
t.onkey(p1.go_up,"Up")
t.onkey(p1.go_down,"Down") 
t.onkey(p2.go_up,"W")
t.onkey(p2.go_down,"S") 
game=True   
while game:
    time.sleep(b.s)
    t.update() 
    b.move_X()
    if(b.ycor()>280 or b.ycor()<-280):
        b.bounce()
    if((b.distance(p1)<50 and b.xcor()>320)):
        b.bounce1() 
    if(b.distance(p2)<50 and b.xcor()<-320):
        b.bounce1()   
    if(b.xcor()>380):
        score.r_points()
        b.goto(0,0)
        b.s=0.1
        b.bounce1()
    if(b.xcor()<-380):
        score.l_points()
        b.goto(0,0)
        b.s=0.1
        b.bounce1()
        


t.exitonclick()    