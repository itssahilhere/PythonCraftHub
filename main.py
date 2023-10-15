from turtle import Turtle,Screen
import random
color_list=["Red", "Orange", "Black", "Green"]
s=Screen()
timy=Turtle()
timy.shape("circle")
timy.speed("fastest")
timy.penup()
timy.setpos(-200,-200)
timy.pendown()
for i in range(1,11):
    for j in range(0,10):
        c=random.choice(color_list)
        timy.dot(20,c)
        timy.penup()
        timy.forward(50)
        timy.pendown()
    if(i%2==0):
        timy.right(90)
        timy.penup()
        timy.forward(50)
        timy.right(90)
        timy.forward(50)
        timy.pendown()
    else:
        timy.left(90)
        timy.penup()
        timy.forward(50)
        timy.left(90)
        timy.forward(50)
        timy.pendown()
timy.hideturtle()
s.exitonclick()