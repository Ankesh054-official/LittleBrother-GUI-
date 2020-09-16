from tkinter import *
from tkinter import messagebox
from core import searchPersonne
from core import settings

# setting switch function:
def switch(self, navself, topFrame, btnState):
    # dictionary of colors:
    color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

    if btnState is True:
            # create animated Navbar closing:
            for x in range(301):
                navself.place(x=-x, y=0)
                topFrame.update()

            # resetting widget colors:
            topFrame.config(bg="#252726")

            # turning button OFF:
            btnState = False
    else:
        # make self dim:
        topFrame.config(bg="#252726")

        # created animated Navbar opening:
        for x in range(-300, 0):
            navself.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

# to show profile if exist
def seeProfle(navself):
    return messagebox.showinfo("info ","seeprofile")

# to show all existing profile in database
def allprofile(navself):
    return messagebox.showinfo("info","allprofile")

def go(name):
    while True:
        if name != '':
            messagebox.showinfo("error","Profile name is required")
    name = name.split(" ")
    name = [i.capitalize() for i in name]
    name = " ".join(name)
    while True:
        # messagebox.askquestion("Profile","Want to register a Twitter account to profile?","yes","no")
        print(question + " Want to register a Twitter account to profile?")
        choixPr = input(" [y/n]: ")
        if choixPr.upper() == 'N':
            break
        else:
            twitter = input("\n Twitter: ")
            info['URL']['Twitter'] = twitter
            break
    # print(found+" %s" % (twitter))
    while True:
        print(question + " Want to register an Instagram account to profile?")
        choixPr = input(" [y/n]: ")
        if choixPr.upper() == 'N':
            break
        else:
            instagram = input("\n Instagram: ")
            info['URL']['Instagram'] = instagram
            break
    while True:
        print(question + " Want to register a Facebook account to profile?")
        choixPr = input(" [y/n]: ")
        if choixPr.upper() == 'N':
            break
        else:
            facebook = input("\n Facebook: ")
            info['URL']['Facebook'] = facebook
            break

    create = pr.writeProfile(fileName=name, path=settings.pathDatabase, info=info)

    if create:
        print("\n" + found + " Profile '% s' has been created successfully." % (name))
    else:
        print("\n" + warning + " An error has occurred. Profile '% s' could not be created." % (name))

# to create a profile
def createprofile(navself):
    navself = Toplevel(navself)
    navself.title("Create Profile")
    navself.minsize(713, 398)
    navself.maxsize(713, 398)
    navself.config(bg="grey17")
    Label(navself, text="Profile Name:", bg="grey17", fg="red", font=("comicsansms", 15, "bold"), relief=FLAT).place(x=5, y=20)
    Label(navself, text="(Format: First name Last name)", bg="grey17", fg="red", font=("comicsansms", 15, "bold"), relief=FLAT).place(x=150 ,y=130)
    name = Entry(navself)
    name.place(x=150 ,y=60) # profile name
    name = name.get()
    Button(navself, text="submit", command=go(name)).place(x=50, y=100)


    # p1 = Entry(navself)
    # p1.place(x=150, y=20)
    # Label(navself, text="(Format: First name Last name)", bg="grey17", fg="red", font=("comicsansms", 10, "bold"),
    #       relief=FLAT).place(x=100, y=50)

    navself.mainloop()

# to decrypte hash
def hashdecrypter(navself):
    return messagebox.showinfo("info","hash")

def Person_lookup(self,lookup):
    lookup.destroy()
    l = Label(self, text="Name:", bg="black", fg="Grey",
              font=("comicsansms", 16, "bold"),relief=FLAT).place(x=230,y=140)
    l = Label(self, text="City/Department:", bg="black", fg="Grey",
              font=("comicsansms", 16, "bold"),relief=FLAT).place(x=230, y=240)
    l = Label(self, text="Last name first name.", bg="black", fg="red",
              font=("comicsansms", 16, "bold"),relief=FLAT).place(x=250, y=180)
    nom = Entry(self, relief=FLAT,  font=("comicsansms", 20, "bold"))
    nom.place(x=380,y=140)
    city = Entry(self, relief=FLAT,  font=("comicsansms", 20, "bold"))
    city.place(x=380,y=240)
    btn = Button(self, text="Search", font="BahnschriftLight 15", bg="gray17", fg="white",
               activebackground="gray17", activeforeground="green", bd=0,
               command=lambda: searchPersonne.searchPersonne(self,nom.get(),city.get(),settings.countrycode)).place(x=300, y=340)

def Mail_tracer(navself):
    return messagebox.showinfo("info", "Mail_tracer")


def Username_lookup(navself):
    return messagebox.showinfo("info", "Username_lookup")


def Employees_search(navself):
    return messagebox.showinfo("info", "Employees_search")


def Lookup_address(navself):
    return messagebox.showinfo("info", "Lookup_address")


def Google_search(navself):
    return messagebox.showinfo("info", "Google_search")


def Phone_lookup(navself):
    return messagebox.showinfo("info", "Phone_lookup")


def Facebook_GraphSearch(navself):
    return messagebox.showinfo("info", "Facebook_GraphSearch")


def IP_lookup(navself):
    return messagebox.showinfo("info", "IP_lookup")


def twitter_info(navself):
    return messagebox.showinfo("info", "twitter_info")


def SSID_locator(navself):
    return messagebox.showinfo("info", "SSID_locator")


def instagram_info(navself):
    return messagebox.showinfo("info","instagram_info")

def Email_lookup(navself):
    return messagebox.showinfo("info","Email_lookup")

def FR(navself):
    return messagebox.showinfo("info","FR")

def LU(navself):
    return messagebox.showinfo("info","LU")

def BE(navself):
    return messagebox.showinfo("info","BE")

def All(navself):
    return messagebox.showinfo("info","ALL")

def CH(navself):
    return messagebox.showinfo("info","CH")
