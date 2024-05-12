from tkinter import *
from tkinter import messagebox
import sqlite3

LOGwindow = None  # Global variable to hold the login window
LOGwindow = Tk()
LOGwindow.geometry("600x600")
LOGwindow.title("Login Page")
LOGwindow.configure(bg="#E8D09C")

conn = sqlite3.connect("account.db") #create / fetch database
c = conn.cursor() #create cursor


#FUNCTIONS ---------------------------------------------------------
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    conn = sqlite3.connect("account.db") #create / fetch database
    c = conn.cursor() #create cursor

    #scans through the table
    c.execute("SELECT * FROM userinfo WHERE username=? AND password=?", (username, password))
    user = c.fetchone() #fetch one as in fetch the ONE that matches. its either match or no match.

    if user: #dont have to explicitly type 'true', it knows.
        messagebox.showinfo("Success", "Login successful!")
        import homescreen
        create_root()
        LOGwindow.destroy()

    elif (username == "meow", password == "1234"):
        import admin
        create_admin()
        LOGwindow.destroy()

    else:
        messagebox.showerror("Error", "Invalid username or password.")



#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)


#FRAME---------------------------------------------------------------
frame=Frame(LOGwindow, bg="#FFFFFF", padx=20, pady=20)


#WIDGETS-------------------------------------------------------------
login_title = Label(frame, text="L O G I N", font=font_30, padx=0, pady=30, bg="#FFFFFF")
username_label = Label(frame, text="Username", font=font_15, padx=30, pady=15, bg="#FFFFFF")
username_entry = Entry(frame, font=font_15, bg="#FFFFFF")
username_entry.get()
password_label = Label(frame, text="Password", font=font_15, padx=30, pady=15, bg="#FFFFFF")
password_entry = Entry(frame, show="•", font=font_15, bg="#FFFFFF")
password_entry.get()

login_button = Button(frame, text="Login", font=font_20, bg="#FFFFFF", relief= "flat", padx=50, command=login)


#pack it in
login_title.grid(row=0, column=1, columnspan=2, sticky="ew")
username_label.grid(row=1, column=1)
username_entry.grid(row=1, column=2)
password_label.grid(row=2, column=1)
password_entry.grid(row=2, column=2)
login_button.grid(row=4, column=1, columnspan=2)
frame.pack(side="top", expand=True)


LOGwindow.mainloop()