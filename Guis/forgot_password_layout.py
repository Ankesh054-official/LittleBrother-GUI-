"""Reset Password Window
   Designed By : ANKESH"""
from tkinter import *
# from PIL import ImageTK
from core import main
from Guis import signin_layout,create_account_layout

def forgot_lay(self,title1):
    self.destroy()
    self = Tk()
    def not_lay():
        x = lambda: main.forgotpassword(e.get())
        if x()==1:
            l = Label(self, text="Check your email for reset link", bg="black", fg="red", font=("comicsansms", 30, "bold"),
                  relief=FLAT).place(x=150, y=400)
            bt = Button(self, activebackground="black", activeforeground="white", text="Signin", bg="white",
                        fg="black", font=("comicsansms", 12, "bold"),
                        relief=SUNKEN, borderwidth=3,
                        command=lambda self=self: signin_layout.signin(self, title1="Signin")).place(x=650, y=600)
        else:
            bt = Button(self, activebackground="black", activeforeground="white", text="Create account", bg="white",
                        fg="black", font=("comicsansms", 12, "bold"),
                        relief=SUNKEN, borderwidth=3,
                        command=lambda self=self: create_account_layout.create_ac(self, title1="Create account")).place(x=650, y=600)
    p1 = PhotoImage(file='res/bit.png')
    self.iconphoto(False, p1)
    height = self.winfo_screenheight()
    width = self.winfo_screenwidth()
    self.maxsize(width, height)
    self.minsize(width - 100, height - 100)
    self.geometry("{0}x{1}+75+75".format(height, width))
    self.title(title1)
    self.config(bg="black")
    img = PhotoImage(file="res/canvalogo1.png")
    label = Label(self, image=img)
    label.place(x=0, y=-1)
    self.title("Reset Password")
    l = Label(self, text="Email", bg="black", fg="Grey", font=("comicsansms", 16, "bold"),
              relief=FLAT).place(x=50, y=200)
    e = Entry(self, relief=FLAT, font=("comicsansms", 20, "bold"))
    e.place(x=250, y=200)
    bt = Button(self, activebackground="black", activeforeground="white", text="RESET", bg="white", fg="black", font=("comicsansms", 12, "bold"),
                relief=SUNKEN, borderwidth=3, command=not_lay).place(x=550,y=600)
    self.mainloop()