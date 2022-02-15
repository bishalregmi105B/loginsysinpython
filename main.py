from tkinter import font
from authorizer import*
from tkinter import *
import tkinter
from login import loginsys

root = tkinter.Tk()
root.geometry("720x270")
root.title("Login System")

def signupsys():
    fm = LabelFrame(root,text="Signup Page")
    fm.pack()

    tkinter.Label(fm,text="Enter Username",font=('24')).grid(row=4,column=4)
    uname = Entry(fm,background="White",foreground="Gray",width="90", font=('Ubuntu', 40))
    uname.grid(row=4,column=10)

    tkinter.Label(fm,text="Enter Your Password",font=('24')).grid(row=9,column=4)
    password = Entry(fm,background="White",foreground="Gray",width="90", font=('Ubuntu', 40))
    password.grid(row=9,column=10)

    tkinter.Label(fm,text="Enter Your Email",font=('24')).grid(row=16,column=4)
    email = Entry(fm,background="White",foreground="Gray",width="90", font=('Ubuntu', 40))
    email.grid(row=16,column=10)

    def createaccount():
        d= signup(uname.get(),password.get(),email.get())
        if d=="succ" and len(password.get())>=8:
            Label(fm,text="Signup Success",height='20').grid(row=30,column=9)
        else:
            print("Signup Failed")
        
            print(len(password.get()))
    btn = Button(fm,text="Signup",background="White",foreground="Gray",width="20",command=createaccount)
    btn.grid(row=27,column=9)

    def login():
        fm.destroy()
        loginsys(root,signupsys)
    btn2 = Button(fm,text="Login Here",background="White",foreground="Gray",width="20",command=login)
    btn2.grid(row=30,column=9)



signupsys()
root.mainloop()