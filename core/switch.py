from tkinter import *
from tkinter import messagebox
from core import searchPersonne
from core import settings


# setting switch function:
def switch(navself, topFrame, btnState):
    # create animated Navbar closing:
    if btnState is True:
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
def seeProfle(profile, navself):
    profile.destroy()
    return messagebox.showinfo("info ","seeprofile")

# to show all existing profile in database
def allprofile(profile, navself):
    profile.destroy()
    return messagebox.showinfo("info","allprofile")


# to create a profile
def createprofile(profile, navself):
    profile.destroy()
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
    Button(navself, text="submit").place(x=50, y=100)


    # p1 = Entry(navself)
    # p1.place(x=150, y=20)
    # Label(navself, text="(Format: First name Last name)", bg="grey17", fg="red", font=("comicsansms", 10, "bold"),
    #       relief=FLAT).place(x=100, y=50)

    navself.mainloop()

# to decrypte hash
def hashdecrypter(more_tools, navself):
    more_tools.destroy()
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

def Mail_tracer(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "Mail_tracer")


def Username_lookup(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "Username_lookup")


def Employees_search(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "Employees_search")


def Lookup_address(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "Lookup_address")


def Google_search(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "Google_search")


def Phone_lookup(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "Phone_lookup")


def Facebook_GraphSearch(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "Facebook_GraphSearch")


def IP_lookup(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "IP_lookup")


def twitter_info(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "twitter_info")


def SSID_locator(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info", "SSID_locator")


def instagram_info(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info","instagram_info")

def Email_lookup(self, lookup):
    lookup.destroy()
    return messagebox.showinfo("info","Email_lookup")

def FR(options, navself):
    options.destroy()
    return messagebox.showinfo("info","FR")

def LU(options, navself):
    options.destroy()
    return messagebox.showinfo("info","LU")

def BE(options, navself):
    options.destroy()
    return messagebox.showinfo("info","BE")

def All(options, navself):
    options.destroy()
    return messagebox.showinfo("info","ALL")

def CH(options, navself):
    options.destroy()
    return messagebox.showinfo("info","CH")
