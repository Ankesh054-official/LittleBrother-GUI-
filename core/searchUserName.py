import requests
from core.searchGoogle import searchGoogle
from colorama import init, Fore,  Back,  Style
from tkinter import *
from tkinter.ttk import *
import time

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

def searchUserName(self, text, username_lookup, username):
	# username = input(" Pseudo: ")
	# Progress bar widget
	progress = Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
	progress.place(x=400, y=140)
	username_lookup.destroy()
	l3 = Label(self, text="Searching... '%s'..." % (username),font=("comicsansms", 16, "bold"))
	l3.place(x=350,y=200)

	progress['value'] = 5
	self.update_idletasks()
	time.sleep(0.1)

	# url = "https://www.google.com/search?num=100&q=\\\"%s\"\\"
	url = "https://www.google.com/search?num=100&q=\\%s\\"

	progress['value'] = 20
	self.update_idletasks()
	time.sleep(0.1)

	url2 = "https://www.google.com/search?num=100&q=\\intitle:\"%s\"\\"
	requete = requests.get(url % (username))

	progress['value'] = 25
	self.update_idletasks()
	time.sleep(0.1)

	requete2 = requests.get(url2 % (username))
	searchGoogle(self, text,progress,l3,requete=requete, requete2=requete2)