""" # Main Console
   Designed By : ANKESH"""
from tkinter import *
from time import sleep
from random import *
from lib.menu import menu
from tkinter import messagebox
from core.switch import switch
from core.navbtn import Profle, main_Help, Feedback, More_Tools, Lookup, About, Change_country


def main_frame(self, Email):
    self.destroy()
    self = Tk()
    p1 = PhotoImage(file='../res/bit.png')
    self.iconphoto(False, p1)
    self.title("LittleBrother")
    self.geometry("1200x900+75+200")
    self.minsize(980, 660)
    self.config(bg="black")
    img = PhotoImage(file="../res/canvalogo1.png")
    lb = Label(self, image=img)
    lb.place(x=5, y=-1)
    sleep(1)
    menu(self,False)
    # dictionary of colors:
    color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}


    # loading Navbar icon image:
    navIcon = PhotoImage(file="../res/menu.png")
    closeIcon = PhotoImage(file="../res/close.png")

    # top Navigation bar:
    topFrame = Frame(self, width=50, bg="#252726")
    topFrame.pack(side=LEFT, fill=Y)

    # setting Navbar frame:
    navself = Frame(self, bg="gray17", height=1000, width=300)
    navself.place(x=-300, y=0)
    Label(navself, font="Bahnschrift 15", bg="#252726", fg="black", height=2, width=300, padx=20).place(x=0,y=0)


    # option in the navbar:
    options = ["Profile", "Lookup","More Tools", "Change country","Main Help", "About", "Feedback"]

    # commands for the navbar:
    work = [lambda: Profle(navself), lambda: Lookup(navself), lambda: More_Tools(navself), lambda: Change_country(navself), lambda: main_Help(navself), lambda: About(navself),lambda: Feedback(navself)]
    # set y-coordinate of Navbar widgets:
    y = 80
    x = 30
    # Navbar Option Buttons:
    for i in range(7):
        x += randrange(5, 20, 5)
        Button(navself, text=options[i], font="BahnschriftLight 15", bg="gray17", fg="white",
               activebackground="gray17", activeforeground="green", bd=0,
               command=work[i]).place(x=x, y=y)
        y += 40
        x -= randrange(10, 20, 5)

    # self = Label(text="WELCOME {0}".format(Email.split("@")[0].upper()), bg="black", fg="white",
    #              font=("comicsansms", 30, "bold"), relief=FLAT)
    # self.master.lift()
    # self.place(x=140, y=30)
    # self.after(1300, lambda: self.destroy())

    # Navbar button:
    navbarBtn = Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20,
                           command= lambda: switch(self, navself, topFrame, btnState=False))
    navbarBtn.place(x=6, y=10)

    # Navbar Close Button:
    closeBtn = Button(navself, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0,
                         command= lambda: switch(self, navself, topFrame, btnState=True))
    closeBtn.place(x=250, y=10)

    self.mainloop()
# main_frame(self="root",Email="ankeshs054@gmail.com")