import ImageTk
from colorama import init, Fore,  Back,  Style
from core.instagramSearchTool import instagramSearchTool, pat, go
from core.shortCutUrl import shortCutUrl
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import wget
import time
from PIL import Image

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"


def searchInstagram(self,instagram_info,user,text):
	global path
	instagram_info.destroy()

	# Progress bar widget
	progress = Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
	progress.place(x=600, y=200)
	# user = input(" Username: ")
	urlProfil = "https://instagram.com/"+user

	progress['value'] = 5
	self.update_idletasks()
	time.sleep(0.1)

	insta = instagramSearchTool()
	insta.getInfo(user)


	progress['value'] = 10
	self.update_idletasks()
	time.sleep(0.1)

	name = insta.name
	userId = insta.id
	images = insta.profi_pic_hd
	try:
		image = shortCutUrl(images)
		username = insta.username

		progress['value'] = 15
		self.update_idletasks()
		time.sleep(0.1)

		private = insta.private
		followers = insta.followers
		friend = insta.friends
		publication = insta.medias

		progress['value'] = 20
		self.update_idletasks()
		time.sleep(0.1)

		bio = insta.biography
		url = insta.url
		email = insta.email
		adresse = insta.adresse
		phone = insta.phone

		progress['value'] = 25
		self.update_idletasks()
		time.sleep(0.1)

		# Set up the image URL
		image_url = "{}".format(images)
		try:
			os.mkdir("{0}/{1}".format(os.getcwd(), user))
		except FileExistsError:
			pass
		image_filename = wget.download(image_url)
		os.system("mv {0} profile.png && mv profile.png {1}/".format(image_url.split('/')[-1].split('?')[0], user))
		load = Image.open("{0}/profile.png".format(user))
		render = ImageTk.PhotoImage(load)
		img = Label(self, image=render)
		img.image = render
		img.place(x=1030, y=10)

		progress['value'] = 30
		self.update_idletasks()
		time.sleep(0.1)

		text.insert(END, "\n[{}]\n".format(username))
		text.insert(END, " Name: {}\n".format(name))
		text.insert(END, " Pictures: {}\n".format(image))
		text.insert(END, " ID: {}\n".format(userId))
		text.insert(END, " Protected: {}\n".format(private))
		text.insert(END, " Subscribers: {}  |  Subscriptions: {}\n".format(followers, friend))
		text.insert(END, " Publication: {}\n".format(publication))
		try:
			text.insert(END, " Bio: {}\n".format(bio))
		except:
			messagebox.showinfo("Unsupported","Sorry But we can't show you Bio's because your computer's terminal does't support emojis.")
			text.insert(END, " Sorry But we can't show you Bio's because your computer's terminal does't support emojis.\n")
		progress['value'] = 50
		self.update_idletasks()
		time.sleep(0.1)

		if url:
			text.insert(END, " Url: {}\n".format(url))
		if email:
			text.insert(END, " Email: {}\n".format(email))
		if phone:
			text.insert(END, " Phone: {}\n".format(phone))
		if adresse:
			text.insert(END, " Places: {}\n".format(adresse))

		if not private:

			while True:
				choix = messagebox.askquestion("Download Image", "Do you want to download the last 12 photos posted?")

				if choix == "" or choix.upper() == "NO":

					progress['value'] = 100
					self.update_idletasks()
					time.sleep(0.1)
					progress.destroy()
					break

				elif choix.upper() == "YES":

					progress['value'] = 70
					self.update_idletasks()
					time.sleep(0.1)

					pathDefault = os.getcwd() + "/" + user
					pat(progress, 70, insta, urlProfil, pathDefault, self, user)
					break
		else:
			messagebox.showinfo("Private Account", "We can't download images from {0}'s Profile.".format(user))
			progress.destroy()
	except TypeError:
		progress.destroy()
		messagebox.showerror("NOT FOUND",user+" user not found")
