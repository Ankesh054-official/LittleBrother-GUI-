from Guis.gui import lay
from tkinter import *
import os,time

try:
    os.system("clear && figlet -c -t  Littlebrother")
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