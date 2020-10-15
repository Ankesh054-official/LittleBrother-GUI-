import requests, re, json
from colorama import init, Fore,  Back,  Style
from terminaltables import SingleTable
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
import time

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"


def ipFinder(self, text, Lookup_ipaddr, ip):
	Lookup_ipaddr.destroy()
	# ip = input(" Adresse IP: ")

	# Progress bar widget
	progress = Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
	progress.place(x=350, y=300)
	l2 = Label(self, text=" Locating {0}...".format(ip))
	l2.place(x=350, y=200)
	# print("\n"+wait+" Locating '%s'..." % (ip))

	TABLE_DATA = []

	url = "http://ip-api.com/json/"
	data = requests.get(url+ip).content.decode('utf-8')
	values = json.loads(data)

	progress['value'] = 20
	self.update_idletasks()
	time.sleep(0.1)

	status = values['status']

	if status != "success":
		messagebox.showerror("Invalid!"," Adresse IP invalid.")
		progress['value'] = 50
		self.update_idletasks()
		time.sleep(0.1)
		progress.destroy()
		l2.destroy()

	else:
		text.insert(END,"[ %s ]" % (ip))
		text.insert(END,"\n IP: " + ip)
		# text.insert(END,"\n Hostname: " + values['ipName'])
		text.insert(END,"\n ISP: " + values['isp'])
		text.insert(END,"\n Organisation: "+values['org'])
		text.insert(END,"\n Pays: " + values['country'])
		text.insert(END,"\n Region: " + values['region'])
		text.insert(END,"\n Ville: " + values['city'])
		localisation = str(values['lat']) + ','+str(values['lon'])
		text.insert(END,"\n Localisation: "+localisation)
		text.insert(END,"\n Maps: https://www.google.fr/maps?q=%s" % (localisation))
		progress['value'] = 100
		self.update_idletasks()
		time.sleep(0.1)
		progress.destroy()
		l2.destroy()