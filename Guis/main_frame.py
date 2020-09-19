""" # Main Console
   Designed By : ANKESH"""
from tkinter import *
from random import *
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
    # dictionary of colors:
    color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}


    # loading Navbar icon image:
    navIcon = PhotoImage(file="../res/menu.png")
    closeIcon = PhotoImage(file="../res/close.png")

    # for text
    textframe = Frame(self, width=90, bg="red")
    textframe.pack(side=RIGHT)

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
    work = [lambda: Profle(self,topFrame,navself), lambda: Lookup(self,topFrame,navself),
            lambda: More_Tools(self,topFrame,navself), lambda: Change_country(self,topFrame,navself),
            lambda: main_Help(self,topFrame,navself), lambda: About(self,topFrame,navself),
            lambda: Feedback(self,topFrame,navself)]
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

    # Navbar button:
    navbarBtn = Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20,
                           command= lambda: switch(navself, topFrame, btnState=False))
    navbarBtn.place(x=6, y=10)

    # Navbar Close Button:
    closeBtn = Button(navself, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0,
                         command= lambda: switch(navself, topFrame, btnState=True))
    closeBtn.place(x=250, y=10)
    text = Text(textframe, width=1200,bg="grey17", fg="white")
    text.insert(INSERT, "Output of any tool will be displayed here.")
    text.pack(side=RIGHT)
    self.mainloop()
# main_frame(self="root",Email="ankeshs054@gmail.com")