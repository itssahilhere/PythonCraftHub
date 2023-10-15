from tkinter import *
window=Tk()
window.title("MY FIRST GUI")
window.minsize(500,300)
label=Label(text="NEW TEXT",font={'arial',12,'bold'})
label.grid(column=0,row=0)
def button_clicked():
    dat=data.get()
    label.config(text=dat)
button=Button(text='CLICK ME',command=button_clicked)
button.grid(row=1,column=1)
# entry
data=Entry(width=10)
data.grid(column=3,row=2)
button1=Button(text='CLICK ME')
button1.grid(row=0,column=2)








window.mainloop()