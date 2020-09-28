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

	# text.insert(END,values)

	# {'status': 'success', 'country': 'India', 'countryCode': 'IN', 'region': 'HR', 'regionName': 'Haryana',
	#  'city': 'Rohtak', 'zip': '124001', 'lat': 28.8964, 'lon': 76.5909, 'timezone': 'Asia/Kolkata',
	#  'isp': 'Reliance Jio Infocomm Limited', 'org': 'Rjil Internet', 'as': 'AS55836 Reliance Jio Infocomm Limited',
	#  'query': '157.36.151.141'}

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

	else:
		# infos = ("IP", ip)
		# TABLE_DATA.append(infos)
		# infos = ("ISP", values['isp'])
		# TABLE_DATA.append(infos)
		# progress['value'] = 40
		# self.update_idletasks()
		# time.sleep(0.1)
		# infos = ("Organisation", values['org'])
		# TABLE_DATA.append(infos)
		# infos = ("Pays", values['country'])
		# TABLE_DATA.append(infos)
		# infos = ("Region", values['regionName'])
		# TABLE_DATA.append(infos)
		# infos = ("Ville", values['city'])
		# progress['value'] = 60
		# self.update_idletasks()
		# time.sleep(0.1)
		# TABLE_DATA.append(infos)
		# infos = ("Code Postal", values['zip'])
		# TABLE_DATA.append(infos)
		# localisation = str(values['lat'])+', '+str(values['lon'])
		# infos = ("Localisation", localisation)
		# TABLE_DATA.append(infos)
		# progress['value'] = 80
		# self.update_idletasks()
		# time.sleep(0.1)
		# infos = ("Maps", "https://www.google.fr/maps?q="+localisation)
		# TABLE_DATA.append(infos)
		# # table = SingleTable(TABLE_DATA, ip)
		# # text.insert(END,table.table)
		#
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