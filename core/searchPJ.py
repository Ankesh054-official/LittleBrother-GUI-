from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
from core.searchInfoNumero import searchInfoNumero
from terminaltables import SingleTable
from colorama import init, Fore,  Back,  Style
import time

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

init()

def searchPJ(progress,self,te, requete='', num=''):
	def testResponse(requete):
		progress['value'] = 35
		self.update_idletasks()
		time.sleep(0.1)
		noReponse = soup.find("p", {"class": "wording-no-responses"})
		if noReponse:
			return 1

	progress['value'] = 30
	self.update_idletasks()
	time.sleep(0.1)

	page = requete.text #content.decode('utf-8')
	soup = BeautifulSoup(page, "html.parser")
	rep = testResponse(requete)
	if rep == 1:
		messagebox.showerror("NO INFO"," No results for your search ... o_o '")
		if num != '':
			pass

	TABLE_DATA = [
		('Name', 'Address', 'Phone', 'Line Phone')
	]

	progress['value'] = 40
	self.update_idletasks()
	time.sleep(0.1)

	profiles_list = soup.find_all("div", {"class":"zone-bi"})
	for profile in profiles_list:
		nameList = [n.text.strip() for n in profile.find_all("a", {"class": "denomination-links pj-lb pj-link"})][0]
		addressList = [a.text.strip() for a in profile.find_all("a", {"class": "adresse pj-lb pj-link"})][0]
		numList = [n.text.strip().replace(" ","") for n in profile.find_all("strong", {"class": "num"})]
		operator_list = []
		for n in numList:
			p = searchInfoNumero()
			p.search(n)
			operator_list.append(p.operator.replace("Mobile - ", ""))

		TABLE_DATA.append((nameList, addressList, ", ".join(numList), ", ".join(operator_list)))
	progress['value'] = 50
	self.update_idletasks()
	time.sleep(0.1)
	if rep != 1:
		table_instance = SingleTable(TABLE_DATA, " Particulier ")
		table_instance.inner_row_border = True
		te.insert(END,table_instance.table)
		progress['value'] = 70
		self.update_idletasks()
		time.sleep(0.1)
		# print("\n"+table_instance.table)