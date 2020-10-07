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

def download_insta_img(progress,value, frame, insta, urlProfil, user, path):
	pictureInfo = insta.get_picturesInfo(urlProfil)
	progress['value'] = value
	frame.update_idletasks()
	time.sleep(0.1)

	for i in pictureInfo:
		try:
			lb.destroy()
		except UnboundLocalError:
			pass
		media = pictureInfo[i]['display']
		typeMedia = pictureInfo[i]['type_media']
		date = pictureInfo[i]['date']
		view = pictureInfo[i]['info']
		loc = pictureInfo[i]['localisation']
		filename = user + '_' + str(i) + ".jpg"
		lb = Label(frame, text="(%s) %s %s [%s] %s downloaded." % (str(i), typeMedia, date, view, loc))
		lb.pack(side=BOTTOM ,fill=X)

		if not loc:
			loc = ''

		insta.downloadPictures(media, user, path, filename)
		progress['value'] += 2
		frame.update_idletasks()
		time.sleep(0.1)
	progress.destroy()
	lb.destroy()
	return messagebox.showinfo("Flag message", " Download Image finished.")
