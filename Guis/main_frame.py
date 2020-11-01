""" # Main Console
   Designed By : ANKESH"""
from tkinter import *
from random import *
from core.switch import switch, Person_lookup
from core.navbtn import Profle, main_Help, Feedback, About
from core.switch import Username_lookup, Employees_search, Lookup_address, Google_search
from core.switch import Phone_lookup,IP_lookup,SSID_locator, instagram_info


def main_frame(self):
    self.destroy()
    self = Tk()
    # p1 = PhotoImage(file='../res/bit.png')
    p1 = PhotoImage(file='res/bit.png')
    self.iconphoto(False, p1)
    self.title("LittleBrother")
    height = self.winfo_screenheight()
    width = self.winfo_screenwidth()
    self.maxsize(width, height)
    self.minsize(width - 100, height - 100)
    self.geometry("{0}x{1}+75+75".format(height, width))
    self.config(bg="black")
    # dictionary of colors:
    color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}
    navIcon = PhotoImage(file="res/menu.png")
    closeIcon = PhotoImage(file="res/close.png")

    # Scroll bar for vertical movement for data:
    h = Scrollbar(self, orient='horizontal')
    h.pack(side=BOTTOM, fill=X)
    v = Scrollbar(self)
    v.pack(side=RIGHT, fill=Y)
    text = Text(self, height=39.35, width=120, bg="grey17", fg="white",  xscrollcommand=h.set,
                yscrollcommand=v.set)
    text.place(x=60, y=10)
    text.insert(1.0,"OUTPUT OF EVERY TOOL WILL BE DISPLAYED HERE")
    h.config(command=text.xview)
    v.config(command=text.yview)

    # top Navigation bar:
    topFrame = Frame(self, width=50, bg="#252726")
    topFrame.pack(side=LEFT, fill=Y)

    # setting Navbar frame:
    navself = Frame(self, bg="gray17", height=1000, width=300)
    navself.place(x=-300, y=0)

    Label(navself, font="Bahnschrift 15", bg="#252726", fg="black", height=2, width=300, padx=20).place(x=0,y=0)

    # option in the navbar:
    options = ["Profile", "Person lookup", "Username lookup", "Employees search", "Lookup address",
               "Google search", "Phone lookup", "IP lookup",
               "SSID locator", "instagram info","Main Help", "About", "Feedback"]

    # commands for the navbar:
    work = [lambda: Profle(self,text,topFrame,navself), lambda: Person_lookup(self, text, navself, topFrame), lambda: Username_lookup(self,text, navself, topFrame),
            lambda: Employees_search(self,text, navself, topFrame),lambda: Lookup_address(self, text, navself, topFrame),
            lambda: Google_search(self, text, navself, topFrame),
            lambda: Phone_lookup(self, text, navself, topFrame),  lambda: IP_lookup(self, text, navself, topFrame),
            lambda: SSID_locator(navself, topFrame), lambda: instagram_info(self,text, navself, topFrame),
            lambda: main_Help(self,topFrame,navself), lambda: About(self,topFrame,navself),
            lambda: Feedback(self,topFrame,navself)]
    # set y-coordinate of Navbar widgets:
    y = 50
    x = 15
    # Navbar Option Buttons:
    for i in range(12):
        Button(navself, text=options[i], font="BahnschriftLight 15", bg="gray17", fg="white",
               activebackground="gray17", activeforeground="green", bd=0, width=19,
               command=work[i]).place(x=x, y=y)
        y += 40

    # Navbar button:
    navbarBtn = Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20,
                           command= lambda: switch(navself, text, topFrame, btnState=False))
    navbarBtn.place(x=6, y=10)

    # Navbar Close Button:
    closeBtn = Button(navself, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0,
                         command= lambda: switch(navself,text,  topFrame, btnState=True))
    closeBtn.place(x=250, y=10)
    self.mainloop()