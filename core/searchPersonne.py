import requests
from tkinter import *
from tkinter.ttk import *
import time
from core.searchPJ import searchPJ
from core.searchInfoNumero import searchInfoNumero
from core.searchYellowLU import searchYellowLU
from core.searchLocalCH import searchLocalCH
from core.searchPageDor import searchPageDor
from core.facebookSearchTool import facebookSearchTool
from core.twitterSearchTool import twitterSearchTool
from core.instagramSearchTool import instagramSearchTool
from core.searchCopainsdavant import searchCopainsdavant
from core.searchPersonneLinkedin import searchPersonneLinkedin
from terminaltables import SingleTable
from colorama import init, Fore,  Back,  Style

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

init()



def searchPersonne(self ,text,person_lookup,nom,city,codemonpays):

	person_lookup.destroy()
	# nom = Entry()
	# nom.place(x=200,y=200)
	# nom = nom.get()
	# print(nom)
	# city = input(" Ville/Departement: ")
	# Progress bar widget
	progress = Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
	progress.place(x=600, y=200)

	try:

		headers = {
			'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
			'referrer': 'https://google.com',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'utf-8',
			'Accept-Language': 'en-US,en;q=0.9',
			'Pragma': 'no-cache'
		}
		progress['value'] = 5
		self.update_idletasks()
		time.sleep(0.1)

		if codemonpays == 'FR':
			# Page Jaune search
			url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={}&ou={}"
			requete = requests.get(url.format(nom, city), headers=headers)
			searchPJ(progress,self,text, requete)

		elif codemonpays == 'BE':
			# Page D'or search
			url = "https://www.pagesblanches.be/chercher/personne/{}/{}/"
			requete = requests.get(url.format(nom, city), headers=headers)
			searchPageDor(text,self,requete)

		elif codemonpays == 'CH':
			# Suisse search
			url = "https://tel.local.ch/fr/q?area={}&city=&company=&ext=1&name={}&phone=&rid=455h&street=&typeref=res"
			searchLocalCH(text,url.format(city, nom))

		elif codemonpays == 'LU':
			# Luxembourg search
			url = "https://www.yellow.lu/fr/pages-blanches/recherche?query={}"
			searchYellowLU(url.format(nom))

		else:
			# Recherche FR
			url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={}&ou={}"
			requete = requests.get(url.format(nom, city), headers=headers)
			searchPJ(progress,self,text, requete)

			# Recherche BE
			url = "https://www.pagesblanches.be/chercher/personne/{}/{}/"
			requete = requests.get(url.format(nom, city), headers=headers)
			searchPageDor(text,self,requete)

			# Recherche CH
			url = "https://tel.local.ch/fr/q?area={}&city=&company=&ext=1&name={}&phone=&rid=455h&street=&typeref=res"
			searchLocalCH(text,url.format(city, nom))

			# Recherche LU
			url = "https://www.yellow.lu/fr/pages-blanches/recherche?query={}"
			searchYellowLU(text,url.format(nom))
		progress['value'] =10
		self.update_idletasks()
		time.sleep(0.1)

		# Copain d'avant search
		searchCopainsdavant(text, nom, city)

		progress['value'] = 15
		self.update_idletasks()
		time.sleep(0.1)

		# LinkedIn search
		searchPersonneLinkedin(text, nom, city)

		# Facebook search
		fbtool = facebookSearchTool()
		accountsFb = fbtool.searchFacebook(nom)

		title = " Facebook "

		TABLE_DATA = [
			('Name', 'User', 'Location'),
		]

		count = 0

		progress['value'] = 25
		self.update_idletasks()
		time.sleep(0.1)

		for a in accountsFb:
			count += 1
			name = a[1]
			username = a[0]
			fbtool.getInfoProfile(username)
			loc = fbtool.address
			if not loc:
				loc = ""

			tuples = (name, username, loc)
			# listeInfos.append(tuples)
			TABLE_DATA.append(tuples)

		progress['value'] = 35
		self.update_idletasks()
		time.sleep(0.1)

		if count > 0:
			table_instance = SingleTable(TABLE_DATA, title)
			text.insert(END,table_instance.table)
			# labl = Label(self, text=table_instance.table, bg="black", fg="green",
			# 			 font=("comicsansms", 15, "bold"), relief=FLAT)
			# labl.place(x=20, y=2)

		# Twitter Search
		title = " Twitter "

		progress['value'] = 50
		self.update_idletasks()
		time.sleep(0.1)

		TABLE_DATA = [
			('Name', 'User', 'Date', 'Location'),
		]

		twitool = twitterSearchTool()
		accountTwitter = twitool.searchTwitter(nom)

		count = 0

		for a in accountTwitter:
			count += 1
			name = a[1]
			username = "@" + a[0]
			twitool.getInfoProfile(a[0])

			location = twitool.location
			date = twitool.birth
			bio = twitool.description
			url = twitool.url

			tuples = (name, username, date, location)
			TABLE_DATA.append(tuples)

		if count > 0:
			table_instance = SingleTable(TABLE_DATA, title)
			text.insert(END,table_instance.table)
			# lb = Label(self, text=table_instance.table, bg="black", fg="red", font=("comicsansms", 10, "bold"),
			# 		   relief=FLAT).place(x=250, y=480)
		# print(table_instance.table)
		# Instagram search

		title = " Instagram "

		instatls = instagramSearchTool()
		instatls.searchInsta(nom)

		accounts = instatls.accounts

		TABLE_DATA = [
			('Name', 'User'),
		]

		count = 0

		progress['value'] = 65
		self.update_idletasks()
		time.sleep(0.1)

		for account in accounts:
			url = "https://instagram.com/" + account
			i = instagramSearchTool()
			i.getInfo(url)
			name = i.name

			tuples = (name, account)
			TABLE_DATA.append(tuples)

			count += 1

		if count > 0:
			progress['value'] = 100
			self.update_idletasks()
			time.sleep(0.1)
			progress.destroy()
			table = SingleTable(TABLE_DATA, title)
			text.insert(END,table.table)
			# lb = Label(self, text=table.table, bg="black", fg="red", font=("comicsansms", 10, "bold"),
			# 		   relief=FLAT).place(x=250, y=480)
	# print(table.table)




	except IOError:
		progress['value'] = 50
		self.update_idletasks()
		time.sleep(0.1)

		progress['value'] = 80
		self.update_idletasks()
		time.sleep(0.1)
		progress.destroy()
		pass
