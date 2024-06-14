from tkinter import *
from tkinter import messagebox
import subprocess
import sys
import sqlite3
import bcrypt

LOGwindow = None  # Global variable to hold the login window
LOGwindow = Tk()
LOGwindow.geometry("600x600")
LOGwindow.title("Login Page")
LOGwindow.configure(bg="#E8D09C") 

conn = sqlite3.connect("database.db") #create / fetch database
c = conn.cursor() #create cursor


#PARAMETER-----------------------------------------------------------l
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)

pathhome = "homescreen.py"
argshome = '"%s" "%s"' % (sys.executable, pathhome)

pathadmin = "admin.py"
argsadmin = '"%s" "%s"' % (sys.executable, pathadmin)

pathreg = "register.py"
argsreg = '"%s" "%s"' % (sys.executable, pathreg)


#FUNCTIONS ---------------------------------------------------------
def redirect_r():
    LOGwindow.destroy()
    proc = subprocess.run(argsreg)


def login():
    global LOGwindow
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    conn = sqlite3.connect("database.db") #create / fetch database
    c = conn.cursor() #create cursor

    #scans through the table
    c.execute("SELECT * FROM userinfo WHERE username=?", (username,))
    user = c.fetchone() #fetch one as in fetch the ONE that matches. its either match or no match.

    if user:
        hashed_password = user[1]
        if bcrypt.checkpw(password.encode(), hashed_password.encode()): #dont have to explicitly type 'true', it knows.
            messagebox.showinfo("Success", "Login successful!")
            LOGwindow.destroy()
            proc = subprocess.run([sys.executable, "homescreen.py", username])
        else:
            messagebox.showerror("Error", "Invalid password.")

    elif (username == "meow" and password == "1234"):
        LOGwindow.destroy()
        proc = subprocess.run(argsadmin)

    else:
        messagebox.showerror("Error", "Invalid username.")


#WIDGETS-------------------------------------------------------------
frame=Frame(LOGwindow, bg="#FFFFFF", padx=20, pady=20)
frame.pack(side="top", expand=True)

login_title = Label(frame, text="L O G I N", font=font_30, padx=0, pady=30, bg="#FFFFFF")
login_title.grid(row=0, column=0, columnspan=2, sticky="ew")

username_label = Label(frame, text="Username", font=font_15, padx=30, pady=15, bg="#FFFFFF")
username_label.grid(row=1, column=0)

username_entry = Entry(frame, font=font_15, bg="#FFFFFF")
username_entry.grid(row=1, column=1)
username_entry.get()

password_label = Label(frame, text="Password", font=font_15, padx=30, pady=15, bg="#FFFFFF")
password_label.grid(row=2, column=0)

password_entry = Entry(frame, show="•", font=font_15, bg="#FFFFFF")
password_entry.grid(row=2, column=1)
password_entry.get()

regbutton = Button(frame, text="Don't have an account, yet? Register here!", font=font_15, fg="navy", bg="#FFFFFF", relief="flat", command=redirect_r)
regbutton.grid(row=3, column=0, columnspan=2, pady=5)

login_button = Button(frame, text="Login", font=font_20, bg="#FFFFFF", padx=50, command=login)
login_button.grid(row=4, column=0, columnspan=2)


LOGwindow.mainloop()