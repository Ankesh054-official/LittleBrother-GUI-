from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
import requests
import time
from core import settings

def check_internet(frame1):
	# Progress bar widget
	progress = Progressbar(frame1, orient = HORIZONTAL, length = 200, mode = 'determinate')
	progress.place(x=210, y=190)
	#Check Internet is conected or not
	global url, timeout
	url = "http://www.kite.com"
	timeout = 5
	try:

		progress['value'] = 5
		frame1.update_idletasks()
		time.sleep(1)

		progress['value'] = 10
		frame1.update_idletasks()
		time.sleep(1)

		progress['value'] = 20
		frame1.update_idletasks()
		time.sleep(1)

		progress['value'] = 30
		frame1.update_idletasks()
		time.sleep(1)

		settings.init()

		progress['value'] = 40
		frame1.update_idletasks()
		time.sleep(1)

		progress['value'] = 50
		frame1.update_idletasks()
		time.sleep(1)

		progress['value'] = 60
		frame1.update_idletasks()

		request = requests.get(url, timeout=timeout)

		progress['value'] = 70
		frame1.update_idletasks()
		time.sleep(1)

		progress['value'] = 80
		frame1.update_idletasks()
		time.sleep(1)

		progress['value'] = 90
		frame1.update_idletasks()
		time.sleep(1)

		progress['value'] = 100
		frame1.update_idletasks()
		time.sleep(0.5)
		progress.destroy()
		return 1

	except (requests.ConnectionError, requests.Timeout) as exception:

		progress['value'] = 70
		progress.destroy()
		return messagebox.showerror('No Internet', "Check your internet connection.")