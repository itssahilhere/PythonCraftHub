from tkinter import *
import pandas
from pandas.core.frame import DataFrame
import random

def next_card():
    global dict,flip_timer,words_learn
    windows.after_cancel(flip_timer)
    canvas.itemconfig(text_french,text="FRENCH",fill='black')
    dict=random.choice(new_dict)
    # words_learn=new_dict.remove(dict)
    canvas.itemconfig(word_french,text=dict['French'],fill="black")
    canvas.itemconfig(front,image=img_front)
    flip_timer=windows.after(3000,func=flip)
def is_known():
    new_dict.remove(dict)
    data=pandas.DataFrame(new_dict)
    data.to_csv("C:/sahil/day 31/words_to_learn.csv",index=False)
    next_card()
def flip():  
    canvas.itemconfig(front,image=img_back)
    canvas.itemconfig(text_french,text="ENGLISH",fill='white')
    canvas.itemconfig(word_french,text=dict['English'],fill='white')

    
BACKGROUND_COLOR = "#B1DDC6"
dict={}
words_learn={}
windows=Tk()
new_dict={}
try:
    
    data=pandas.read_csv("C:/sahil/day 31/words_to_learn.csv")
except FileNotFoundError:
    or_data=pandas.read_csv("C:/sahil/day 31/french_words.csv")
    new_dict=or_data.to_dict(orient='records')
else:
    new_dict=data.to_dict(orient='records')
windows.minsize()
windows.title("flashy")
windows.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=windows.after(3000,func=flip)
# windows.after_cancel()
img_front=PhotoImage(file="day 31/card_front.png")
img_back=PhotoImage(file="day 31\card_back.png")
canvas=Canvas(width=800,height=526)
front=canvas.create_image(400,263,image=img_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
text_french=canvas.create_text(400,150,text="",font=('Ariel',40,'italic'))
word_french=canvas.create_text(400,263,text="",font=('Ariel',60,'bold'))
canvas.grid(row=0,column=0,columnspan=2)
my_wrong = PhotoImage(file="C:/sahil/day 31/wrong.png")
my_right=PhotoImage(file="day 31/right.png")
wrong = Button(image=my_wrong,command=next_card, highlightthickness=0)
wrong.grid(column=0,row=1)
right= Button(image=my_right,command=is_known, highlightthickness=0)
right.grid(column=1,row=1)

# button_clicked_right()
# words_learn.Data
next_card()





























windows.mainloop()