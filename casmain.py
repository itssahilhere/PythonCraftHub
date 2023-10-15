import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import Scoreboard
pla=Player()
c1=CarManager()
sc=Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    c1.create()
    c1.move()
    screen.onkey(pla.move,'Up')
    for i in c1.all:
        if(pla.distance(i)<20):
            sc.game_over()
            game_is_on=False
    if(pla.finish()):
        pla.refresh()
        sc.level()
        c1.level_up()
screen.exitonclick()    