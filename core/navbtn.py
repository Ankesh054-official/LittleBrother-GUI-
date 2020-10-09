from tkinter import *
from lib.Url import Url
from core.switch import switch, createprofile, allprofile, seeProfle, hashdecrypter, Person_lookup
from core.switch import Username_lookup, Employees_search, Lookup_address, Google_search
from core.switch import Phone_lookup,IP_lookup,SSID_locator, instagram_info
from core.switch import FR, LU, BE, All, CH


# for profile
def Profle(self, topFrame, navself):
    profile = Toplevel(navself)
    profile.title("Profile")
    profile.minsize(713, 398)
    profile.maxsize(713, 398)
    profile.config(bg="grey17")
    Label(profile, text="Profile Name:", bg="grey17", fg="red", font=("comicsansms", 15, "bold"), relief=FLAT).place(
        x=5, y=20)
    Label(profile, text="(Format: First name Last name)", bg="grey17", fg="red", font=("comicsansms", 15, "bold"),
          relief=FLAT).place(x=150, y=130)
    name = Entry(profile)
    name.place(x=150, y=60)  # profile name
    name = name.get()
    Button(profile, text="submit").place(x=50, y=100)
    switch(navself,topFrame,btnState=True)
    profile.mainloop()


# for more tools
def More_Tools(self, topFrame, navself):
    # option in the navbar:
    options = ["Hash decrypter"]
    work = [lambda: hashdecrypter(more_tools, navself)]
    more_tools = Toplevel(navself)
    more_tools.geometry("300x685+0+55")
    more_tools.minsize(300,685)
    more_tools.maxsize(300,685)
    more_tools.config(bg="grey17")
    more_tools.title("More Tools")
    # Navbar Option Buttons:
    y = 10
    x = 22
    for i in range(1):
        Button(more_tools, text=options[i], font="BahnschriftLight 15", bg="gray17", fg="white",
               activebackground="gray17", activeforeground="green", bd=0,
               command=work[i]).place(x=x, y=y)
        y += 40
    switch(navself,topFrame,btnState=True)

    more_tools.mainloop()


# for help
def main_Help(self, topFrame, navself):
    # option in the navbar:
    options = """
     Action
     ------
    Do some research on a person.
    Use tools other than recognition.
    Create a '.txt' file to write the information obtained.
    Access the database.
    
    Exit the software.
    Displays this message.
    Clear the screen.
    Clear the screen.
    
    """
    name = """                         
 Name                   
 ----                  
 Lookup                 
 Other Tool             
 Make file              
 Show Database          

 Exit                   
 Help                   
 Clear                  
                 
    
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

    # label for help
    La = Label(left, text=name, bg="grey17", fg="white", font=("comicsansms", 20, "bold"), relief=FLAT).pack()
    La = Label(right, text=options, bg="grey17", fg="white", font=("comicsansms", 20, "bold"), relief=FLAT).pack()
    Button(right, activebackground="black", activeforeground="white", text="Exit", bg="white",
           fg="black", font=("comicsansms", 9, "bold"),
           relief=SUNKEN, borderwidth=3, command=lambda: help.destroy()).place(x=480, y=10)
    switch(navself,topFrame,btnState=True)

    # help.mainloop()
    return

# for lookup
def Lookup(self, text, topFrame, navself):
    text.delete(1.0,END)
    lookup = Toplevel(navself)
    # option in the navbar:
    options = ["Person lookup", "Username lookup", "Employees search", "Lookup address",
               "Google search", "Phone lookup", "IP lookup",
               "SSID locator", "instagram info"]
    work = [lambda: Person_lookup(self, text, lookup), lambda: Username_lookup(self,text, lookup),
            lambda: Employees_search(self,text, lookup),lambda: Lookup_address(self, text, lookup),
            lambda: Google_search(self, text, lookup),
            lambda: Phone_lookup(self, text,lookup),  lambda: IP_lookup(self, text, lookup),
            lambda: SSID_locator(lookup), lambda: instagram_info(self,text,lookup),]
    lookup.geometry("300x685+0+55")
    lookup.minsize(300,685)
    lookup.maxsize(300,685)
    lookup.config(bg="grey17")
    lookup.title("Lookup")
    # Navbar Option Buttons:
    y = 10
    x = 22
    for i in range(9):
        Button(lookup, text=options[i], font="BahnschriftLight 15", bg="gray17", fg="white",
               activebackground="gray17", activeforeground="green", bd=0,
               command=work[i]).place(x=x, y=y)
        y += 40
    switch(navself,topFrame,btnState=True)
    lookup.mainloop()


#for about
def About(self, topFrame, navself):
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
          font=("comicsansms", 14, "bold"), relief=FLAT).place(x=10, y=200)
    Label(About, text="Developed BY: \n\t\t\t\t\t\t\tFRONTEND + Joining BACKEND: ANKESH\t", bg="grey17", fg="white",
          font=("comicsansms", 9, "bold"), relief=FLAT).pack(side=BOTTOM, anchor=NE)
    Button(About, activebackground="black", activeforeground="white", text="Exit", bg="white",
                fg="black", font=("comicsansms", 8, "bold"),
                relief=SUNKEN, borderwidth=3, command=lambda: About.destroy()).place(x=1250, y=10)
    switch(navself,topFrame,btnState=True)

    # About.mainloop()
    return

#for feedback
def Feedback(self, topFrame, navself):
    feedback = Toplevel(navself)
    feedback.geometry("1200x900+75+200")
    feedback.config(bg="grey17")
    feedback.title("Feedback")

    link1 = Label(feedback, activebackground="black", activeforeground="white", bg="white",
                fg="black", font=("comicsansms", 13, "bold"),
                relief=SUNKEN, borderwidth=3, text="Register Issue", cursor="hand2")
    link1.place(x=300,y=200)
    link1.bind("<Button-1>", lambda e: Url.callback("https://github.com/Ankesh054-official/LittleBrother-GUI-/issues/new"))

    link2 = Label(feedback, activebackground="black", activeforeground="white", bg="white",
                fg="black", font=("comicsansms", 13, "bold"),
                relief=SUNKEN, borderwidth=3, text="Support",  cursor="hand2")
    link2.place(x=800,y=200)
    link2.bind("<Button-1>", lambda e: Url.callback("mailto:littlebrother.cyber@gmail.com"))

    Label(feedback, text="Developed BY: \n\t\t\t\t\t\t\tFRONTEND + Joining BACKEND: ANKESH\t", bg="grey17", fg="white",
          font=("comicsansms", 9, "bold"), relief=FLAT).pack(side=BOTTOM, anchor=NE)
    switch(navself,topFrame,btnState=True)

    feedback.mainloop()

# for change country
def Change_country(self, topFrame, navself):
    # option in the navbar:
    options = ["FR (France)", "LU (Luxembourg)", "BE (Belgique)", "All (FR, BE, CH, LU)", "CH (Suisse)"]
    work = [lambda: FR(options, navself), lambda: LU(options, navself), lambda: BE(options, navself),
            lambda: All(options, navself), lambda: CH(options, navself)]
    changecountry = Toplevel(navself)
    changecountry.geometry("300x685+0+55")
    changecountry.minsize(300,685)
    changecountry.maxsize(300,685)
    changecountry.config(bg="grey17")
    changecountry.title("Change Country")
    # Navbar Option Buttons:
    y = 10
    x = 22
    for i in range(5):
        Button(changecountry, text=options[i], font="BahnschriftLight 15", bg="gray17", fg="white",
               activebackground="gray17", activeforeground="green", bd=0,
               command=work[i]).place(x=x, y=y)
        y += 40
    switch(navself,topFrame,btnState=True)

    # changecountry.mainloop()
    return

