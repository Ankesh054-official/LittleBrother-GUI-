import pyrebase
from tkinter import *
from tkinter import messagebox
from Guis import main_frame, signin_layout
import requests

def login(frame1, Email, Password):
    firebaseConfig = {
        "apiKey": "AIzaSyCPCLf2oLLfXY-gzzGiR8JH4l9Z1EO_BqU",
        "authDomain": "python-tkinter-login.firebaseapp.com",
        "databaseURL": "https://python-tkinter-login.firebaseio.com",
        "projectId": "python-tkinter-login",
        "storageBucket": "python-tkinter-login.appspot.com",
        "messagingSenderId": "323517919210",
        "appId": "1:323517919210:web:cc72da9dfc9ea80d188c93",
        "measurementId": "G-PLX0C2HTR5"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    try:
        try:
            login = auth.sign_in_with_email_and_password(email=Email, password=Password)
            # divert to the little brother console
            main_frame.main_frame(frame1)
        except requests.exceptions.ConnectionError:
            return messagebox.showinfo("Connection Error!", "Internet Disconnected")
    except requests.exceptions.HTTPError:
        return messagebox.showerror("SIGNIN_INVALID", "MAYBE, INVALID_EMAIL\nor\nINVALID_PASSWORD")


def create_ac(frame1, Email, Password):
    firebaseConfig = {
        "apiKey": "AIzaSyCPCLf2oLLfXY-gzzGiR8JH4l9Z1EO_BqU",
        "authDomain": "python-tkinter-login.firebaseapp.com",
        "databaseURL": "https://python-tkinter-login.firebaseio.com",
        "projectId": "python-tkinter-login",
        "storageBucket": "python-tkinter-login.appspot.com",
        "messagingSenderId": "323517919210",
        "appId": "1:323517919210:web:cc72da9dfc9ea80d188c93",
        "measurementId": "G-PLX0C2HTR5"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    try:
        user = auth.create_user_with_email_and_password(email=Email, password=Password)
        auth.send_email_verification(id_token=user['idToken'])
        messagebox.showinfo("Verification", "You have received an verification Email\nSo:\nVerify your Email:")
        signin_layout.signin(frame1,"SignIn")
    except requests.exceptions.HTTPError:
        return messagebox.showinfo("EMAIL EXIST","ACCOUNT ALREADY EXIST:")


def terms_and_conditions():
    # terms and conditions
    root = Tk()
    root.title("Terms and Conditions")
    root.geometry("1200x900+300+200")
    root.minsize(980, 660)
    root.config(bg="black")
    Label(root, text="Welcome to LittleBrother" ,font=("comicsansms", 45, "bold"), bg="black",
          fg="white", relief=FLAT).place(x=50, y=40)
    Label(root, text="{0}".format('LittleBrother is an information collection tool (OSINT), It is basically a CLI '
                                      'based tool which aims to carry out research on a French, Swiss,\n Luxembourgish '
                                    'or Belgian person.It provides various modules that allow efficient '
                                    'searches. LittleBrother does not require an API key or login ID.\n\n'
                                      'This is a extended version of LittleBrother tool, It is a GUI based tool.'
                                      'We need some of your information to run this tool properly, We promise you not\n'
                                      ' to leak your data and try to make it more secure.'), bg="black", fg="white",
          font=("comicsansms", 15, "bold"), relief=FLAT).place(x=130, y=200)
    bt = Button(root, activebackground="black", activeforeground="white", text="Exit", bg="white",
                fg="black", font=("comicsansms", 9, "bold"),
                relief=SUNKEN, borderwidth=3, command=lambda: root.destroy()).place(x=1250, y=10)
    root.mainloop()


def forgotpassword(email):
    firebaseConfig = {
        "apiKey": "AIzaSyCPCLf2oLLfXY-gzzGiR8JH4l9Z1EO_BqU",
        "authDomain": "python-tkinter-login.firebaseapp.com",
        "databaseURL": "https://python-tkinter-login.firebaseio.com",
        "projectId": "python-tkinter-login",
        "storageBucket": "python-tkinter-login.appspot.com",
        "messagingSenderId": "323517919210",
        "appId": "1:323517919210:web:cc72da9dfc9ea80d188c93",
        "measurementId": "G-PLX0C2HTR5"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    try:
        auth.send_password_reset_email(email=email)
        return 1
    except:
        return messagebox.showerror("Not Found", "EMAIL_NOT_FOUND")
