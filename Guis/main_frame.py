""" # Main Console
   Designed By : ANKESH"""
from tkinter import *
from tkinter import messagebox

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

    # Menubar
    menubar = Menu(self, bg="black", fg="white", font=("comicsansms", 12, "bold"))

    menubar.add_command(label="Profile", font=("comicsansms", 12, "bold"), command=lambda: messagebox.showinfo("DATA FLOW","PROFILE")) # add command (profile function).

    more = Menu(menubar, bg="black", fg="white", tearoff=0)
    more.add_command(label="Hash Decrypter", font=("comicsansms", 12, "bold"), command=lambda: messagebox.showinfo("DATA FLOW","Hash Decrypter")) # add command (function of Hash Decrypter).
    more.add_command(label="Profiler", font=("comicsansms", 12, "bold"), command=lambda: messagebox.showinfo("DATA FLOW","Profiler")) # add command (function of Profiler).
    more.add_separator()
    more.add_command(label="Exit", font=("comicsansms", 12, "bold"), command=self.destroy)
    menubar.add_cascade(label="More Tools", menu=more)

    help = Menu(menubar, bg="black", fg="white", tearoff=0)
    help.add_command(label="About", font=("comicsansms", 12, "bold"), command=lambda: messagebox.showinfo("DATA FLOW","ABOUT")) # add command (function of About).
    menubar.add_cascade(label="Help", menu=help)

    self.config(menu=menubar)

    self = Label(text="WELCOME {0}".format(Email.split("@")[0].upper()), bg="black", fg="white",
                  font=("comicsansms", 30, "bold"), relief=FLAT)
    self.master.lift()
    self.place(x=140, y=300)
    self.after(1000, lambda: self.destroy())
    self.mainloop()
