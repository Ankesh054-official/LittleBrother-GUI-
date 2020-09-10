from tkinter import *
from random import *
from core.switch import switch
from tkinter import messagebox


# for profile
def Profle():
    print("profile")

# for more tools
def More_Tools():
    pass

# for help
def Help():
    pass

# for lookup
def Lookup(navself, btnState, topFrame, ):
    # option in the navbar:
    options = ["Person lookup", "Mail tracer", "Username lookup", "Employees search", "Lookup address",
               "Google search", "Phone lookup", "Facebook GraphSearch", "IP lookup", "twitter info",
               "SSID locator", "instagram info", "Email lookup"]
    lookup = Toplevel(navself)
    # Navbar Option Buttons:
    y = 80
    x = 22
    for i in range(13):
        x += randrange(5, 20, 5)
        Button(lookup, text=options[i], font="BahnschriftLight 15", bg="gray17", fg="white",
               activebackground="gray17", activeforeground="green", bd=0,
               command=[i]).place(x=x, y=y)
        y += 40
        x -= randrange(10, 20, 5)


#for about
def About():
    pass

#for feedback
def Feedback():
    pass

# for change country
def Change_country():
    pass

