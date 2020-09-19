from colorama import init, Fore,  Back,  Style
from core.instagramSearchTool import instagramSearchTool
from core.shortCutUrl import shortCutUrl
import os
from tkinter import *

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

def searchInstagram(user,text):
	# user = input(" Username: ")
	urlProfil = "https://instagram.com/"+user

	insta = instagramSearchTool()
	insta.getInfo(user)

	name = insta.name
	userId = insta.id
	images = insta.profi_pic_hd
	images = shortCutUrl(images)
	username = insta.username
	private = insta.private
	followers = insta.followers
	friend = insta.friends
	publication = insta.medias
	bio = insta.biography
	url = insta.url
	email = insta.email
	adresse = insta.adresse
	phone = insta.phone


	text.insert(END,"\n[{}]\n".format(username))
	text.insert(END," Name: {}\n".format(name))
	text.insert(END," Pictures: {}\n".format(images))
	text.insert(END," ID: {}\n".format(userId))
	text.insert(END," Protected: {}\n".format(private))
	text.insert(END," Abonnés: {}  |  Abonnements: {}\n".format(followers, friend))
	text.insert(END," Publication: {}\n".format(publication))
	text.insert(END," Bio: {}\n".format(bio))

	if url:
		text.insert(END," Url: {}\n".format(url))
	if email:
		text.insert(END," Email: {}\n".format(email))
	if phone:
		text.insert(END," Telephone: {}\n".format(phone))
	if adresse:
		text.insert(END," Lieux: {}\n".format(adresse))

	if not private:
		print("\n"+question+" Voulez vous télécharger les 12 dernières photos postées ?")

		while True:
			choix = input("\n [o/N]: ")

			if choix == "" or choix.upper() == "N":
				break
			
			elif choix.upper() == "O":
				print("\n"+question+" Ou voulez-vous enregistrer les photos ?")
				pathDefault = os.getcwd()
				print(Fore.YELLOW+" Default path: "+pathDefault+Fore.RESET)
				path = input("\n Path: ")
				print("\n"+wait+" Téléchargement des photos de '%s'\n" % (user))
			
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
					print("(%s) %s %s [%s] %s téléchargé." % (str(i), typeMedia, date, view, loc))

				print("\n"+found+" Téléchargement fini.")
				break