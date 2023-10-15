from turtle import Turtle,Screen
timmy=Turtle()
s=Screen()
s.listen()
def forward():
    timmy.forward(15)
def backward():
    timmy.backward(15)
def clockwise():
    timmy.right(15)
def anticlock():
    timmy.left(15)
def clears():
    timmy.clearscreen()    

s.onkeypress(fun=forward, key='f')
s.onkeypress(fun=backward, key='b')
s.onkeypress(fun=clockwise, key='c')
s.onkeypress(fun=anticlock, key='a')
s.onkeypress(fun=clears, key='d')
s.exitonclick()