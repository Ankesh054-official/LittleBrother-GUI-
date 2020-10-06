""" #  Create account window
   Designed By : Ankesh
   """

from tkinter import *
from tkinter import messagebox
from core import main
from Guis import signin_layout


def create_ac(self, title1):
    self.destroy()
    self = Tk()
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
    var = IntVar()
    dic = ["Create", "Signin", "Exit", "Accept Terms and Conditions"]
    endis = ["First Name", "Last Name", "Email", "Password", "Confirm Password"]
    lb = Label(self, text="Create Your Account", bg="black", fg="white", font=("comicsansms", 30, "bold"), relief=FLAT)
    lb.place(x=500, y=20)
    lb = Label(self, text="If you already have an account, then make ", bg="black", fg="grey",
               font=("comicsansms", 12, "bold"), relief=FLAT)
    lb.place(x=500, y=650)
    y, indec = 150, 0
    for i in endis:
        if i == "Confirm Password":
            lb = Label(self,
                       text="Password should contain Uppercase characters,\n Lowercase characters ,Numbers "
                            ", Symbols", bg="black", fg="red", font=("comicsansms", 10, "bold"), relief=FLAT
                       )
            lb.place(x=250, y=480)
        lb = Label(self, text="{0}".format(endis[indec]), bg="black", fg="Grey", font=("comicsansms", 16, "bold"),
                   relief=FLAT)
        lb.place(x=50, y=y)
        y += 100
        indec += 1
        e0 = Entry(self, relief=FLAT, font=("comicsansms", 20, "bold"))
        e0.place(x=250, y=140)  # pack entry
        e1 = Entry(self, relief=FLAT,  font=("comicsansms", 20, "bold"))
        e1.place(x=250, y=240)  # pack entry
        e2 = Entry(self, relief=FLAT, font=("comicsansms", 20, "bold"))
        e2.place(x=250, y=340)  # pack entry
        e3 = Entry(self, relief=FLAT, show="*", font=("comicsansms", 20, "bold"))
        e3.place(x=250, y=440)  # pack entry
        e4 = Entry(self, relief=FLAT, show="*", font=("comicsansms", 20, "bold"))
        e4.place(x=250, y=540)  # pack entry

    def enter():
        if e3.get() == e4.get():  # try to make strongest password using capital let.small let,num, symbols
            if len(e3.get()) >= 8:
                if var.get() == 1:
                    main.create_ac(self, e2.get(), e3.get())
                else:
                    messagebox.showerror("Error!", "You have to accept our Terms and Condition.")
            else:
                return messagebox.showerror("Error!", "Password < 8,\n It should be password >= 8.")
        else:
            return messagebox.showerror("Error!", "Confirm your password:")
    bt = Button(self, activebackground="black", activeforeground="white", text="{0}".format(dic[0]), bg="white",
                fg="black", font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=3, command=enter)
    bt.place(x=550, y=600)
    bt = Button(self, activebackground="black", activeforeground="white", text="{0}".format(dic[1]), bg="black",
                fg="blue", font=("comicsansms", 7, "bold"), relief=FLAT, borderwidth=-1,
                command=lambda: signin_layout.signin(self, title1="{0}".format(dic[1])))
    bt.place(x=800, y=650)
    bt = Button(self, activebackground="black", activeforeground="white", text="{0}".format(dic[2]), bg="white",
                fg="black", font=("comicsansms", 9, "bold"), relief=SUNKEN, borderwidth=3,
                command=lambda: self.destroy())
    bt.place(x=1286, y=10)
    Checkbutton(self, bg="black", bd=3, variable=var).place(x=(80 - 25), y=600)
    bt = Button(self, activebackground="black", activeforeground="white", text="{0}".format(dic[3]), bg="black",
                fg="blue", font=("comicsansms", 12, "bold"), relief=FLAT, borderwidth=-1,
                command=lambda: main.terms_and_conditions())
    bt.place(x=80, y=600)
    self.mainloop()
