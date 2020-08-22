import time, random
from core.Profiler import *
from colorama import Fore
from core import settings
from datetime import date
from txt.text import text
from txt.header import lb_header
from tkinter import *

def checkVersion():
	version = sys.version[:1]
	if int(version) == 3:
		pass
	else:
		sys.exit(warning+" Veuillez lancer la version 3 de python.")

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def times():
	times = time.strftime("%H:%M:%S")
	times = str(times)
	return(times)

def menu(self):
	pr = Profiler()
	pr.loadDatabase(settings.pathDatabase)
	sizeOfDB = pr.size
	nbProfilesBDD = pr.count

	menu = """
Time:      [ %s | %s ]\n
Time Zone: [ %s ]\n
Author:    [ ANKESH054 ]\n
Version:   [ %s ]\n
Country:   [ %s | %s ]\n
Region:	[ %s | %s ]\n
Pin Code:  [ %s ]\n
ISP:       [ %s ]\n
Gateways:  [ %s ]\n
Public Ip: [ %s ]\n
Database:  [ %s | %s Ko ]\n
                %s
	"""

	print(lb_header())
	print(menu% (Fore.YELLOW + str(date.today()) + Fore.RESET,  # for date
				 Fore.YELLOW + times() + Fore.RESET,  # for time
				 Fore.YELLOW + str(settings.timezone) + Fore.RESET,  # timezone
				 Fore.YELLOW + str(settings.version) + Fore.RESET,  # version
				 Fore.CYAN + settings.country + Fore.RESET,  # Country
				 settings.countrycode,  # countrycode
				 Fore.CYAN + str(settings.Region) + Fore.RESET, Fore.YELLOW + str(settings.Regionname) + Fore.RESET,  # Region
				 Fore.YELLOW + str(settings.zip) + Fore.RESET,  # Pincode
				 settings.isp, Fore.GREEN + settings.org + Fore.RESET,
				 Fore.YELLOW + str(settings.query) + Fore.RESET,
				 Fore.GREEN + str(nbProfilesBDD) + Fore.RESET, Fore.RED + str(sizeOfDB) + Fore.RESET,  #database
				 random.choice(text)# txt
		  ))
	return Label(self, text="{0}".format(menu% (str(date.today()),  # for date
												times(),  # for time
												str(settings.timezone),  # timezone
												str(settings.version),  # version
												settings.country,  # Country
												settings.countrycode,  # countrycode
												str(settings.Region), str(settings.Regionname),  # Region
												str(settings.zip),  # Pincode
												settings.isp, settings.org,
												str(settings.query),
												str(nbProfilesBDD), str(sizeOfDB),  #database
												random.choice(text)# txt
		  )), bg="black", fg="white",
		  font=("comicsansms", 15, "bold"), relief=FLAT).place(x=140, y=200)

