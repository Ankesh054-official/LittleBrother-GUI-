""" # Main Console
   Designed By : ANKESH"""
from tkinter import *


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
    self = Label(text="WELCOME {0}".format(Email.split("@")[0].upper()), bg="black", fg="white",
                  font=("comicsansms", 30, "bold"), relief=FLAT)
    self.master.lift()
    self.place(x=140, y=300)
    self.after(1000, lambda: self.destroy())
    self.mainloop()
