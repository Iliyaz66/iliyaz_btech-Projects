from tkinter import *
import random
import string
mw = Tk()
mw.geometry("400x400")
mw.resizable(False,False)
passstr=StringVar()
user_name=StringVar()
pwd_len = IntVar()
accepted_passwords = []
def get_pass():
    pass1=string.ascii_letters+string.digits+string.punctuation
    password=""
    for x in range(pwd_len.get()):
        password=password+random.choice(pass1)
        passstr.set(password)
def saved():
    name=user_name.get()
    passcode=passstr.get()
    print()
    print("User_Name:",name)
    print("Accepted_password:",passcode)
def remove():
    passstr.set("")
    pwd_len.set("")
    user_name.set("")
lb1=Label(mw,text="PASSWORD GENERATOR",bg="skyblue",font="arial 18").pack()
lb2=Label(mw,bg="pink",text="Enter user name").place(x=15,y=54)
e1=Entry(mw,width=10,textvariable=user_name).place(x=200,y=55)
lb3=Label(mw,bg="pink",text="Enter the length of the password").place(x=15,y=97)
e2=Entry(mw,width=10,textvariable=pwd_len).place(x=200,y=100)
lb4=Label(mw,bg="pink",text="Genterated Password").place(x=15,y=140)
e3=Entry(mw,textvariable=passstr,width=30).place(x=200,y=140)

bt1=Button(mw,bg="orange",text="Generatepassword",command=get_pass).place(x=140,y=200)
bt2=Button(mw,text="Accept",bg="green",command=saved).place(x=170,y=250)
bt3=Button(mw,text="Reset",bg="red",command=lambda:remove()).place(x=174,y=300)

mw.mainloop()