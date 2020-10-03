from core.LinkedIn import searchLinkedIn
from colorama import init, Fore,  Back,  Style
from terminaltables import SingleTable
from tkinter import *


warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"

def searchPersonneLinkedin(self,progress,text,nom, city):
	linkedin = searchLinkedIn()
	linkedin.search(progress,self,nom, city)
	found = linkedin.found

	if found:
		employee = linkedin.employees
		profile = linkedin.profiles

		regroup = zip(employee, profile)

		TABLE_DATA = [
			("Name", "Url"),
		] 

		for r in regroup:
			TABLE_DATA.append(r)

		table = SingleTable(TABLE_DATA, title=" LinkedIn ")
		text.insert(END,table.table)
		# labl = Label(self, text=table.table, bg="black", fg="green",
		# 			 font=("comicsansms", 15, "bold"), relief=FLAT)
		# labl.place(x=20, y=2)
