# Facing window/Welcome Screen
#    Designed By : ANKESH
from tkinter import *
from core import layout_decision, loading


def lay(frame1):
    frame1.title("LITTLE BROTHER")

    # Checks Internet is connected or not,raise error accordingly.
    def ch():
        if loading.check_internet(frame1) != 1:
            ch()
    ch()
    btn1 = Button(frame1, activebackground="black", activeforeground="white", text="Register",
                  font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=3, command=lambda:
                  layout_decision.create_lay(frame1, "Create Account")).place(x=115, y=100)
    btn2 = Button(frame1, activebackground="black", activeforeground="white", text="SignIn",
                  font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=3,
                  command=lambda: layout_decision.create_lay(frame1, "SignIn")).place(x=115, y=150)
    btn3 = Button(frame1, activebackground="black", activeforeground="white", text="Forgot Password",
                  font=("comicsansms", 12, "bold"), relief=SUNKEN, borderwidth=3,
                  command=lambda: layout_decision.create_lay(frame1, "Forgot Password")).place(x=115, y=200)

