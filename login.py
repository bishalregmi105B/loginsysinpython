from authorizer import*
from tkinter import *
import tkinter

def loginsys(root,signupsys):

    fm = LabelFrame(root,text="Login Page")
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

    def signup():
        fm.destroy()
        signupsys()

    def loginact():
        d= login(uname.get(),password.get(),email.get())
        if d=="succ" and len(password.get()) >=8:
            print("Login Success")
        else:
            print("Login Failed. Enter Correct Data")
    

    btn1 = Button(fm,text="Login",background="White",foreground="Gray",width="20",command=loginact)
    btn1.grid(row=27,column=9)

    btn = Button(fm,text="Signup Here",background="White",foreground="Gray",width="20",command=signup)
    btn.grid(row=30,column=9)

    


