import requests
from core.searchGoogle import searchGoogle
from colorama import init, Fore,  Back,  Style
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
import time

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
information = "["+Fore.BLUE+"I"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

def google(self, text, goog, nom):
	goog.destroy()
	# Progress bar widget
	progress = Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
	progress.place(x=350, y=300)
	l2 = Label(self, text=" Currently researching...")
	l2.place(x=350, y=200)
	# print("\n"+information+" Renseignez Prénom, Nom, Ville, Département, Sport, Etablissement scolaire ...\n")
	# nom = input(" Recherche: ")
	# print("\n"+wait+" Recherche en cours...")
	url = "https://www.google.com/search?num=20&q=\\%s\\"
	try:
		nom2 = nom.split(" ")
		nom = nom2[0]+'+'+nom2[1]
	except:
		pass
	progress['value'] = 10
	self.update_idletasks()
	time.sleep(0.1)
	requete = requests.get(url % (nom))
	progress['value'] = 20
	self.update_idletasks()
	time.sleep(0.1)
	searchGoogle(self, text,progress,l2,requete=requete)
