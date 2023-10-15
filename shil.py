from turtle import Turtle,Screen
import random
l=[]
s=Screen()
winner=""
s.setup(width=500,height=500)
u=s.textinput(title="MAKE YOUR BET",prompt='WHICH TURTLE WOUULD WIN THE RACE')
is_race_on=False
d=0
colour=['red','blue','yellow','green','orange','violet']
for i in range(0,6):
    timmy=Turtle(shape='turtle')
    timmy.speed('fast')
    timmy.color(colour[i])
    timmy.penup()
    timmy.goto(x=-225,y=-220+d)
    l.append(timmy)
    d+=88
if u:
    is_race_on=True
while is_race_on:
    for i in l:
        if(i.xcor()>220):
            is_race_on=False
            w=i.pencolor()
        t=random.randint(0,10)
        i.forward(t)        
if(w==u):
    print("YOU WON")
else:
    print("YOU LOSS")
    print(f"the winner is {w}")    

s.exitonclick()    

    
