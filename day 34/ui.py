from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizzInterface:
    def __init__(self,quizo:QuizBrain):
        self.quiz=quizo
        self.window=Tk()
        self.window.title("QUIZZLER")
        self.window.config(padx=50,pady=50,bg=THEME_COLOR)
        self.score=Label(text=f"Score:{0}",fg='white',bg=THEME_COLOR)
        self.score.grid(row=0,column=1)
        self.canvas=Canvas(width=300,height=250,bg='white')
        self.quote_text = self.canvas.create_text(150, 125,width=280, text="",font=("Arial", 30, "italic"),fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.right=PhotoImage(file="day 34/true.png")
        self.right_button=Button(image=self.right,command=self.right,highlightthickness=0)
        self.right_button.grid(row=2,column=0)
        self.wrong=PhotoImage(file="day 34/false.png")
        self.wrong_button=Button(image=self.wrong,command=self.wrong,highlightthickness=0)
        self.wrong_button.grid(row=2,column=1)
        self.next_question()
    def next_question(self):
        if(self.quiz.still_has_questions):

            self.canvas.config(bg='white')
            self.score.config(text=f"Score:{self.quiz.score}",fg='white',bg=THEME_COLOR)
            tex=self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text,text=tex)
        else:
            self.canvas.itemconfig(self.quote_text,text="YOU HAVE REACHED LIMIT")  
            self.right_button.config(state="disabled")  
            self.wrong_button.config(state="disabled") 
    def right(self):
        self.feedback(self.quiz.check_answer("true"))
    def wrong(self):
        self.feedback(self.quiz.check_answer("false"))    
    def feedback(self,ans):
        if(ans):

            self.window.after(1000,self.canvas.config(bg='green'))
            self.canvas.config(bg='white')
        else:
            self.window.after(1000,self.canvas.config(bg='red'))
            self.canvas.config(bg='white')




        self.window.mainloop()
    
