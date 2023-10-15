from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search_button():
    try:

        with open("my_data.json",'r') as f:
            data=json.load(f)
    except:
        messagebox.showinfo(title="alert",message="NO SUCH WEBSITE") 
    else:           
        web=web_entry.get()
        try: 
            website=data[web]

        except:
            messagebox.showerror("NO DATA FOUND")
        else:    
            pas=website['password']
            mail=website['mail']
            messagebox.showinfo(title=web,message=f"password: {pas}/n mail: {mail}")


def generte_click():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(letters) for _ in range(nr_symbols)]
    password_numbers=[random.choice(letters) for _ in range(nr_numbers)]

    password_list=password_letters+password_numbers+password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    app=web_entry.get()
    password=pass_entry.get()
    mail=mail_entry.get()
    new_data={
        app:{"password":password,
            "mail":mail,
            }
        }
    if(len(app)==0 or len(mail)==0 or len(password)==0):
        messagebox.showinfo(title="Oops some fields are empty!!!")
    else:
        try:
            with open("my_data.json",'r') as f:
                data=json.load(f)
        except FileNotFoundError:
            with open("my_data.json",'w') as f:
                json.dump(new_data,f,indent=4)    
        else:
            data.update(new_data)
            with open("my_data.json",'w') as f:
                json.dump(data,f,indent=4)
        finally:            
            web_entry.delete(0,END)
            pass_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
windows=Tk()
windows.minsize(500,300)
windows.title("PASSWORD MANAGER")
windows.config(padx=20,pady=20)
img=PhotoImage(file="day 30\logo.png")
canvas=Canvas(width=200,height=200)
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)
website=Label(text="Website:",font=('arial',12,'bold'))
website.grid(row=2,column=0)
web_entry=Entry(width=35)
web_entry.grid(column=1,row=2,columnspan=2)
web_entry.focus()
mail=Label(text="Email/Username:",font=('arial',12,'bold'))
mail.grid(column=0,row=4)
mail_entry=Entry(width=35)
mail_entry.grid(column=1,row=4,columnspan=2)
mail_entry.insert(0,"agarwalsahil123420@gmail.com")
password=Label(text="Password:",font=('arial',12,'bold'))
password.grid(row=6,column=0)
pass_entry=Entry(width=26)
pass_entry.grid(row=6,column=1)
generate=Button(text="generate",command=generte_click)
generate.grid(column=2,row=6)
add=Button(text="Add",command=save,width=36)
add.grid(column=1,row=8,columnspan=2)
search=Button(text="Search",command=search_button)
search.grid(column=2,row=2)



windows.mainloop()