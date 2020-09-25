import time

import requests
import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

def download(url, user, path, filename):
	r = requests.get(url)
	try:
		f = open(path+filename,'wb');
	except FileNotFoundError:
		os.mkdir(path,user)

	for chunk in r.iter_content(chunk_size=255): 
		if chunk:
			f.write(chunk)

	f.close()

def download_insta_img(value, frame, insta, urlProfil, user, path):
	# Progress bar widget
	progress = Progressbar(frame, orient=HORIZONTAL, length=200, mode='determinate')
	progress.pack()
	pictureInfo = insta.get_picturesInfo(urlProfil)

	progress['value'] = value
	frame.update_idletasks()
	time.sleep(0.1)
	Label(frame).pack()

	for i in pictureInfo:
		Label.forget(frame)
		media = pictureInfo[i]['display']
		typeMedia = pictureInfo[i]['type_media']
		date = pictureInfo[i]['date']
		view = pictureInfo[i]['info']
		loc = pictureInfo[i]['localisation']
		filename = user + '_' + str(i) + ".jpg"

		if not loc:
			loc = ''

		insta.downloadPictures(media, user, path, filename)
		progress['value'] += 5
		frame.update_idletasks()
		time.sleep(0.1)
		Label(frame, text="(%s) %s %s [%s] %s downloaded." % (str(i), typeMedia, date, view, loc)).pack()
	progress.destroy()
	messagebox.showinfo("Flag message", " Download Image finished.")
