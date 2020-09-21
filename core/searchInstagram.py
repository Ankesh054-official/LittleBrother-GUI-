from colorama import init, Fore,  Back,  Style
from core.instagramSearchTool import instagramSearchTool
from core.shortCutUrl import shortCutUrl
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import wget
import time

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

def searchInstagram(self,instagram_info,user,text):

	# Progress bar widget
	progress = Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
	progress.place(x=600, y=200)
	# user = input(" Username: ")
	urlProfil = "https://instagram.com/"+user

	insta = instagramSearchTool()
	insta.getInfo(user)

	progress['value'] = 5
	self.update_idletasks()
	time.sleep(0.1)

	name = insta.name
	userId = insta.id
	images = insta.profi_pic_hd
	image = shortCutUrl(images)
	username = insta.username
	private = insta.private
	followers = insta.followers
	friend = insta.friends
	publication = insta.medias

	progress['value'] = 10
	self.update_idletasks()
	time.sleep(0.1)

	bio = insta.biography
	url = insta.url
	email = insta.email
	adresse = insta.adresse
	phone = insta.phone

	# Set up the image URL
	image_url = "{}".format(images)
	image_filename = wget.download(image_url)
	img = PhotoImage(file='{}'.format(image_url.split('/')[-1].split('?')[0]))

	progress['value'] = 30
	self.update_idletasks()
	time.sleep(0.1)

	panel = Label(text, width=50, height=50, image=img)
	panel.place(x=1100, y=20)
	text.insert(END,"\n[{}]\n".format(username))
	text.insert(END," Name: {}\n".format(name))
	text.insert(END," Pictures: {}\n".format(image))
	text.insert(END," ID: {}\n".format(userId))
	text.insert(END," Protected: {}\n".format(private))
	text.insert(END," Subscribers: {}  |  Subscriptions: {}\n".format(followers, friend))
	text.insert(END," Publication: {}\n".format(publication))
	text.insert(END," Bio: {}\n".format(bio))

	progress['value'] = 50
	self.update_idletasks()
	time.sleep(0.1)

	if url:
		text.insert(END," Url: {}\n".format(url))
	if email:
		text.insert(END," Email: {}\n".format(email))
	if phone:
		text.insert(END," Phone: {}\n".format(phone))
	if adresse:
		text.insert(END," Places: {}\n".format(adresse))

	if not private:
		messagebox.askquestion("Download Image","Do you want to download the last 12 photos posted?")
		# print("\n"+question+" Do you want to download the last 12 photos posted? ?")

		while True:
			choix = input("\n [Y/N]: ")

			if choix == "" or choix.upper() == "N":

				progress['value'] = 60
				self.update_idletasks()
				time.sleep(0.1)

				break
			
			elif choix.upper() == "Y":

				progress['value'] = 70
				self.update_idletasks()
				time.sleep(0.1)

				print("\n"+question+" Or do you want to save the photos ?")
				pathDefault = os.getcwd()
				print(Fore.YELLOW+" Default path: "+pathDefault+Fore.RESET)
				path = input("\n Path: ")
				print("\n"+wait+" Upload photos from '%s'\n" % (user))
			
				if not path:
					path = pathDefault
			
				pictureInfo = insta.get_picturesInfo(urlProfil)

				for i in pictureInfo:
					media = pictureInfo[i]['display']
					typeMedia = pictureInfo[i]['type_media']
					date = pictureInfo[i]['date']
					view = pictureInfo[i]['info']
					loc = pictureInfo[i]['localisation'] 
					filename = user+'_'+str(i)+".jpg"

					if not loc:
						loc = ''

					insta.downloadPictures(media, path, filename)
					print("(%s) %s %s [%s] %s downloaded." % (str(i), typeMedia, date, view, loc))

				print("\n"+found+" Download finished.")

				progress['value'] = 100
				self.update_idletasks()
				time.sleep(0.1)
				break