from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as d: 
            self.highscore=int(d.read())
        self.color("white")
        self.penup()
        self.goto(x=0,y=270)
        self.update()
        self.hideturtle()
        

    def update(self):
        self.clear()
        self.write(f"SCORE:{self.score} HIGHSCORE:{self.highscore}",align="center",font=("Arial",24,"normal"))
    #   def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align="center",font=("Arial",54,"normal"))
    def inc_score(self):
        self.score+=1
        self.update()
    def reset_highscore(self):
        if(self.score>self.highscore):
            self.highscore=self.score
            with open("data.txt",mode='w') as file:
                file.write(f"{self.highscore}")
        self.score=0
        self.update()