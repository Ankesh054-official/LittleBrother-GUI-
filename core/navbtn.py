from tkinter import *
from random import *
from core.switch import switch
from tkinter import messagebox


# for profile
def Profle(navself):
    # option in the navbar:
    options = [" Profile", "Show all Profiles", "Create profile"]
    profile = Toplevel(navself)
    profile.geometry("300x685+0+55")
    profile.config(bg="grey17")
    profile.title("Profile")
    # Navbar Option Buttons:
    y = 10
    x = 22
    for i in range(3):
        Button(profile, text=options[i], font="BahnschriftLight 15", bg="gray17", fg="white",
               activebackground="gray17", activeforeground="green", bd=0,
               command=[i]).place(x=x, y=y)
        y += 40
    profile.mainloop()


# for more tools
def More_Tools(navself):
    # option in the navbar:
    options = ["Hash decrypter"]
    more_tools = Toplevel(navself)
    more_tools.geometry("300x685+0+55")
    more_tools.config(bg="grey17")
    more_tools.title("More Tools")
    # Navbar Option Buttons:
    y = 10
    x = 22
    for i in range(1):
        Button(more_tools, text=options[i], font="BahnschriftLight 15", bg="gray17", fg="white",
               activebackground="gray17", activeforeground="green", bd=0,
               command=[i]).place(x=x, y=y)
        y += 40
    more_tools.mainloop()


# for help
def Help(navself):
    # option in the navbar:
    options = """
     Action
     ------
    Make searches with a name, first name and (city).
    Do some research with a username.
    Do some research with an address.
    Do some research with a phone number.
    Make searches with an IP address.
    Search with a MAC / BSSID address
    Do some research with an email address.
    Do research with the header of an email.
    Finds the employees of a company.
    Do some research on google.
    Do research using graphSearch.
    Retrieve information from a Twitter account.
    Retrieve information from an Instagram account.
    
    Return to the main menu.
    To quit the software.
    Clear the screen.
    Display this message.
    
    """
    name = """
     Name                             
     ----                             
    [1] Person lookup                 
    [2] Username lookup               
    [3] Address lookup                
    [4] Phone lookup                  
    [5] IP lookup                     
    [6] SSID locator                  
    [7] Email lookup                  
    [8] Mail tracer                   
    [9] Employees search              
    [10] Google search                
    [11] Facebook graphSearch         
    [12] twitter info                 
    [13] instagram info               
    
    [b] Back main menu                
    [e] Exit script                   
    [c] Clear screen                  
    [h] Help Message                  
    
    """
    help = Toplevel(navself)
    help.geometry("1200x900+75+200")
    help.config(bg="grey17")
    help.title("Help")

    # top Navigation bar:
    left = Frame(help, width=600, bg="#252726")
    left.pack(side=LEFT, fill=Y)

    # setting Navbar frame:
    right = Frame(help, bg="gray17",  width=600)
    right.pack(side=RIGHT, fill=Y)
    Label(navself, font="Bahnschrift 15", bg="#252726", fg="black", height=2, width=300, padx=20).place(x=0, y=0)

    # label for help
    La = Label(left, text=name, bg="grey17", fg="white", font=("comicsansms", 20, "bold"), relief=FLAT).pack()
    La = Label(right, text=options, bg="grey17", fg="white", font=("comicsansms", 20, "bold"), relief=FLAT).pack()
    help.mainloop()


# for lookup
def Lookup(navself):
    # option in the navbar:
    options = ["Person lookup", "Mail tracer", "Username lookup", "Employees search", "Lookup address",
               "Google search", "Phone lookup", "Facebook GraphSearch", "IP lookup", "twitter info",
               "SSID locator", "instagram info", "Email lookup"]
    lookup = Toplevel(navself)
    lookup.geometry("300x685+0+55")
    lookup.config(bg="grey17")
    lookup.title("Lookup")
    # Navbar Option Buttons:
    y = 10
    x = 22
    for i in range(13):
        Button(lookup, text=options[i], font="BahnschriftLight 15", bg="gray17", fg="white",
               activebackground="gray17", activeforeground="green", bd=0,
               command=[i]).place(x=x, y=y)
        y += 40
    lookup.mainloop()


#for about
def About(navself):
    # option in the navbar:
    options = ["","","","",""]
    About = Toplevel(navself)
    About.geometry("1200x900+75+200")
    About.config(bg="grey17")
    About.title("About")
    # label for About
    Label(About, text="{0}".format('LittleBrother is an information collection tool (OSINT), It is basically a CLI '
                                  'based tool which aims to carry out research on\n a French, Swiss, Luxembourgish '
                                  'or Belgian person.It provides various modules that allow efficient '
                                  'searches. \nLittleBrother does not require an API key or login\n ID.'
                                  'This is a extended version of LittleBrother tool, It is a GUI based tool.\n\n'
                                  'We need some of your information to run this tool properly, We promise you not\n'
                                  ' to leak your data and try to make it more secure.'), bg="grey17", fg="white",
          font=("comicsansms", 20, "bold"), relief=FLAT).place(x=10, y=200)
    Label(About, text="Developed BY: \n\t\t\t\t\t\t\tFRONTEND + Joining BACKEND: ANKESH\t", bg="grey17", fg="white",
          font=("comicsansms", 13, "bold"), relief=FLAT).pack(side=BOTTOM, anchor=NE)
    Button(About, activebackground="black", activeforeground="white", text="Exit", bg="white",
                fg="black", font=("comicsansms", 9, "bold"),
                relief=SUNKEN, borderwidth=3, command=lambda: About.destroy()).place(x=1250, y=10)
    About.mainloop()

#for feedback
def Feedback(navself):
    # option in the navbar:
    options = ["","","",""]
    feedback = Toplevel(navself)
    feedback.geometry("1200x900+75+200")
    feedback.config(bg="grey17")
    feedback.title("Feedback")
    # Navbar Option Buttons:
    y = 10
    x = 22
    for i in range(4):
        Button(feedback, text=options[i], font="BahnschriftLight 15", bg="gray17", fg="white",
               activebackground="gray17", activeforeground="green", bd=0,
               command=[i]).place(x=x, y=y)
        y += 40
    feedback.mainloop()


# for change country
def Change_country(navself):
    # option in the navbar:
    options = ["FR (France)", "LU (Luxembourg)", "BE (Belgique)", "All (FR, BE, CH, LU)", "CH (Suisse)"]
    changecountry = Toplevel(navself)
    changecountry.geometry("300x685+0+55")
    changecountry.config(bg="grey17")
    changecountry.title("Change Country")
    # Navbar Option Buttons:
    y = 10
    x = 22
    for i in range(5):
        Button(changecountry, text=options[i], font="BahnschriftLight 15", bg="gray17", fg="white",
               activebackground="gray17", activeforeground="green", bd=0,
               command=[i]).place(x=x, y=y)
        y += 40
    changecountry.mainloop()


