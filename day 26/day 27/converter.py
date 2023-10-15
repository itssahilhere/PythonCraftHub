from tkinter import *
window=Tk()

def button_clicked():
    dat=float(data.get())
    valu=dat * 1.609
    valu=round(valu)
    val.config(text=f"{valu}") 

window.title("MILES TO KM CONVERTER")
window.minsize(500,300)
window.config(padx=100,pady=100)

data=Entry(width=10)
data.grid(column=2,row=2)

miles=Label(text="MILES",font={'arial',12,'bold'})
miles.grid(column=4,row=2)
miles.config(padx=10,pady=10)

label=Label(text="Is Equal To",font={'arial',12,'bold'})
label.grid(column=0,row=4)
label.config(padx=10,pady=10)

valu=0
val=Label(text=f"{valu}",font={'arial',12,'bold'})
val.grid(column=2,row=4)
val.config(padx=10,pady=10)

km=Label(text="KM",font={'arial',12,'bold'})
km.grid(column=4,row=4)
km.config(padx=10,pady=10)

button=Button(text='Calculate',command=button_clicked)
button.grid(column=2,row=5)
































window.mainloop()