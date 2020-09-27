import requests
from core.searchLocalCH import searchLocalCH
from core.searchYellowLU import searchYellowLU
from core.searchPJ import searchPJ
from colorama import init, Fore,  Back,  Style
from tkinter import *
from tkinter.ttk import Progressbar
import time

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

init()

def searchAdresse(self, text, Lookup_addr ,adresse, codemonpays):
	Lookup_addr.destroy()
	# adresse = input(" Adresse: ")
	# clear()
	# Progress bar widget
	progress = Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
	progress.place(x=600, y=300)
	l2 = Label(self, text=" Searching {0}...".format(adresse))
	l2.place(x=350, y=200)
	# print("\n"+wait+" Recherche '%s'..." % (adresse))

	headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	    'referrer': 'https://google.com',
    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    	'Accept-Encoding': 'gzip, deflate, br',
    	'Accept-Language': 'en-US,en;q=0.9',
    	'Pragma': 'no-cache'
    }

	progress['value'] = 20
	self.update_idletasks()
	time.sleep(0.1)

	if codemonpays == "FR":
		# search PageBlanche
		url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=&ou="
		requete = requests.get(url+adresse, headers=headers)
		searchPJ(progress,self,text, requete)

		progress['value'] = 80
		self.update_idletasks()
		time.sleep(0.1)

	elif codemonpays == "CH":
		# search tel.local.hc
		url = "https://tel.local.ch/fr/q?ext=1&name=&company=&street={}&city=&area="
		searchLocalCH(progress, self, text, url.format(adresse))

		progress['value'] = 80
		self.update_idletasks()
		time.sleep(0.1)

	else:
		# Recherche FR
		url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=&ou="
		requete = requests.get(url+adresse, headers=headers)
		searchPJ(progress,self,text,requete)

		progress['value'] = 60
		self.update_idletasks()
		time.sleep(0.1)

		# Recherche CH
		url = "https://tel.local.ch/fr/q?ext=1&name=&company=&street={}&city=&area="
		searchLocalCH(progress, self, text, url.format(adresse))

		progress['value'] = 80
		self.update_idletasks()
		time.sleep(0.1)

	progress['value'] = 100
	self.update_idletasks()
	time.sleep(0.1)
	progress.destroy()
	l2.destroy()