from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN=25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def button_clicked_reset():
    window.after_cancel()
    canvas.itemconfig(text,text="00:00")
    label.config(text="TIMER")
    tick.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def button_clicked_start():
    global reps
    reps+=1
    WORK_SEC=WORK_MIN*60
    LONG_BREAK_SEC=LONG_BREAK_MIN*60
    SHORT_BREAK_SEC=SHORT_BREAK_MIN*60
    if(reps==1 or reps==3 or reps==7):
        
        count_down(WORK_SEC)
        label.config(text="WORK",fg=GREEN)
    if(reps==2 or reps==4 or reps==6):
        count_down(SHORT_BREAK_SEC)
        label.config(text="BREAK",fg=PINK)
    if(reps==8):
        
        count_down(LONG_BREAK_SEC)
        label.config(text="BREAK",fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    min=count//60
    sec=count%60
    if(sec<10):
        sec=f"0{sec}"
    canvas.itemconfig(text,text=f"{min}:{sec}")
    if(count>0):
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        button_clicked_start()
        mark=""
        for _ in range(reps//2):
            mark+="🗸"
        tick.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("PODOROMA")
window.config(padx=100,pady=50,bg=YELLOW)
label=Label(text="TIMER",font=(FONT_NAME,50,'bold'),fg=GREEN,bg=YELLOW)
label.grid(column=2,row=2)
img=PhotoImage(file="C:/sahil/day29/tomato.png")
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=img)
text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=3)
# count_down(5)
start=Button(text='START',command=button_clicked_start,highlightthickness=0)
start.grid(column=1,row=5)
reset=Button(text='RESET',command=button_clicked_reset,highlightthickness=0)
reset.grid(column=3,row=5)
tick=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"bold"))
tick.grid(column=2,row=7)








window.mainloop()