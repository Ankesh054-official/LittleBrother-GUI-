import time

import requests
from tkinter import *
from bs4 import BeautifulSoup
from terminaltables import SingleTable

def searchLocalCH(progress, self, text,url):
	data = requests.get(url).content.decode("utf-8")

	soup = BeautifulSoup(data, "html.parser") 

	nameList = soup.find_all("span", {"class": "listing-title"})
	adresseList = soup.find_all("div", {"class": "listing-address small"})
	phoneList = soup.find_all("a", {"class": "btn btn-sm listing-contact-phone lui-margin-right-xs number phone-number"})

	nameList2 = []
	adresseList2 = []
	phoneList2 = []

	progress['value'] = 30
	self.update_idletasks()
	time.sleep(0.1)

	for name in nameList:
		nameList2.append(name.string.strip())

	for adress in adresseList:
		adresseList2.append(adress.string.strip())

	for phone in phoneList:
		phoneList2.append(phone.getText().replace("*", "").strip())

	regroup = zip(nameList2,adresseList2, phoneList2)

	progress['value'] = 40
	self.update_idletasks()
	time.sleep(0.1)

	TABLE_DATA = [
		("Name", "Adresse", "Telephone"),
	]

	for r in regroup:
		TABLE_DATA.append(r)

	progress['value'] = 60
	self.update_idletasks()
	time.sleep(0.1)

	table = SingleTable(TABLE_DATA, title="Yellow")
	text.insert(END,table.table)

	progress['value'] = 70
	self.update_idletasks()
	time.sleep(0.1)
	# print(table.table)