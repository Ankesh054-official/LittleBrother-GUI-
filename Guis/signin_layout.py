""" #  Signin window
   Designed By : ANKESH"""
from tkinter import *
from tkinter import messagebox
from core import main
from Guis import create_account_layout,forgot_password_layout


def signin(self,title1):
    self.destroy()
    self = Tk()
    p1 = PhotoImage(file='res/bit.png')
    self.iconphoto(False, p1)
    self.geometry("1200x900+75+200")
    self.minsize(980, 660)
    self.title(title1)
    self.config(bg="black")
    img = PhotoImage(file="res/canvalogo1.png")
    label = Label(self, image=img)
    label.place(x=0, y=-1)
    dic = ["Signin", "Create Account", "Exit", "Forgot Password"]
    endis = ["Email", "Password"]
    lb = Label(self, text="SignIn to your Account", bg="black", fg="white", font=("comicsansms", 30, "bold"),
               relief=FLAT).place(x=500, y=20)
    lb = Label(self, text="If you are a new user than ,", bg="black", fg="white", font=("comicsansms", 12, "bold"),
               relief=FLAT).place(x=610,y=650)
    y, n = 150, None
    for i in endis:
        l = Label(self, text="{0}".format(i), bg="black", fg="Grey", font=("comicsansms", 16, "bold"),
                  relief=FLAT).place(x=50, y=y)
        y += 100
    e0 = Entry(self, relief=FLAT, font=("comicsansms", 20, "bold"))
    e0.place(x=250, y=140)
    e1 = Entry(self, relief=FLAT, show="*", font=("comicsansms", 20, "bold"))
    e1.place(x=250, y=240)
    e0.insert(END,"ankeshs054@gmail.com")
    e1.insert(END,"beahacker")
    bt1 = Button(self, activebackground="black", activeforeground="white", text="{0}".format(dic[0]), bg="white", fg="black", font=("comicsansms", 12, "bold"),
                    relief=SUNKEN, borderwidth=3, command=lambda frame1=self: main.login(frame1,e0.get(),e1.get())).place(
            x=550, y=600)
    bt2 = Button(self, activebackground="black", activeforeground="white", text="{0}".format(dic[1]), bg="black", fg="blue", font=("comicsansms", 7, "bold"),
                relief=FLAT, borderwidth=-1, command=lambda self=self: create_account_layout.create_ac(self,title1="{0}".format(dic[1]))).place(x=800,
                                                                                                          y=650)
    bt3 = Button(self, activebackground="black", activeforeground="white", text="{0}".format(dic[2]), bg="white", fg="black", font=("comicsansms", 9, "bold"),
                relief=SUNKEN, borderwidth=3, command=lambda: self.destroy()).place(x=1286, y=10)
    bt4 = Button(self, activebackground="black", activeforeground="white", text="{0}".format(dic[3]), bg="black", fg="blue", font=("comicsansms", 12, "bold"),
                relief=FLAT, borderwidth=-1, command=lambda self=self: forgot_password_layout.forgot_lay(self,title1="{0}".format(dic[-1]))).place(x=80,y=600)
    self.mainloop()