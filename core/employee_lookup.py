# -*- coding: utf-8 -*-

from core.LinkedIn import searchLinkedIn
from colorama import init, Fore,  Back,  Style
from terminaltables import SingleTable
from tkinter import *
from tkinter.ttk import *
import time

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

init()

def employee_lookup(self, text, Employees_search, entre, ciy):
	entreprise = entre.get()
	city = ciy.get()
	Employees_search.destroy()
	l2 = Label(self,text = "Searching for employees of {0}...".format(entreprise))
	l2.place(x=350,y=200)

	# Progress bar widget
	progress = Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
	progress.place(x=400, y=140)

	linkedin = searchLinkedIn()

	progress['value'] = 5
	self.update_idletasks()
	time.sleep(0.1)

	linkedin.search(progress,self,entreprise, city)
	
	found = linkedin.found

	if found:
		employee = linkedin.employees

		TABLE_DATA = [
			("Num", "Name"),
		] 

		x = 1
		for employe in employee:
			TABLE_DATA.append((x, employe))
			x += 1
			progress['value'] += 5
			self.update_idletasks()
			time.sleep(0.1)
		table = SingleTable(TABLE_DATA, title=" LinkedIn ")
		progress['value'] = 100
		self.update_idletasks()
		time.sleep(0.1)
		progress.destroy()
		text.insert(END,table.table)
	l2.destroy()