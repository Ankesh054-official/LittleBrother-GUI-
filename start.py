from Guis.gui import lay
from tkinter import *
import os,time
import platform

def welcome(inp_para):
    f = open('./txt/font.json','r')
    x = f.read()
    f.close()
    y = x.replace('{','')
    z  = y.replace('}','')
    x = z.split(",")

    font = {}

    for i in x:
            font[((i.split(':')[0]).replace('\n',''))] = i.split(':')[1]

    #print(font)

    text = {}
    #inp = input('enter text\t').upper()
    inp = inp_para
    inp = inp.upper()
    for i in inp:
            text['{0}'.format(i.upper())] = (font['"{0}"'.format(i)]).split('\n')

    for i in range(1,8):
            for j in inp:
    #               pass
                    print(text['{0}'.format(j)][i], end=" ")
            print()

def check_exist(f):
    x = ("beautifulsoup4","bs4","colorama","emoji","gcloud","googleapis-common-protos","html5lib",
           "httplib2","jws","mechanize","oauth2client","Pillow","protobuf","pyasn1","pyasn1-modules",
           "pycryptodome","pyparsing","Pyrebase","python-jwt","regex","requests","requests-toolbelt",
           "rsa","six","soupsieve","terminaltables","webencodings","wget")
    for i in x:
        if i not in f.read():
            return False
        
    return True
            

try:
    with open("requirements.txt","r") as f:
            print("Checking requirements ......")
            
            if not check_exist(f):
                print("Installing requirements ......")
                os.system("pip3 install pyrebase && pip3 install --upgrade setuptools && pip3 install --upgrade gcloud && pip3 install pyrebase")
                os.system("pip3 install -r requirements.txt")

            if check_exist(f):
                  os.system("pip freeze> requirements.txt")


    if(platform.system() == "Windows"):
        os.system("cls")

    if(platform.system() !=  "Windows"):
        os.system("clear")

    welcome('Little')
    welcome('Brother')
    root = Tk()
    root.geometry('713x398+300+200')
    root.minsize(713, 398)
    root.maxsize(713, 398)
    root.config(bg="black")
    p1 = PhotoImage(file='res/bit.png')
    root.iconphoto(False, p1)
    img = PhotoImage(file="res/canvalogo.png")
    label = Label(root, image=img)
    label.place(x=-1, y=-1)
    lay(root)  # first window
    root.mainloop()
except:
    os.system('echo {0}'.format("FORCE EXIT"))
    time.sleep(5)
finally:
    os.system('echo bye')