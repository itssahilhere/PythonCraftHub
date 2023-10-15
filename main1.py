from turtle import Screen
from snake import Snake 
from food import Food
from score import Score
import time
s=Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.tracer(0)
is_game_on=True
snake=Snake()
food=Food()
score=Score()
s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")
while is_game_on:
    s.update()
    time.sleep(0.1)
    snake.move()
    if(snake.head.distance(food)<15):
        food.refresh()
        snake.exten()
        score.inc_score()
        # DETECT COLLISIION WITH WALL
    if(snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>270 or snake.head.ycor()<-280):
        score.reset_highscore()
        snake.reset_snake()
        #detection of collision of snake head with tail
    for segment in snake.segment:
        if(snake.head==segment):
            pass
        elif(snake.head.distance(segment)<10):
            score.reset_highscore()  
            snake.reset_snake()
s.exitonclick()

