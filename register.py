from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess
import sys
import bcrypt


REGwindow = Tk()
REGwindow.geometry("600x600")
REGwindow.title("Registration")
REGwindow.configure(bg="#E8D09C")


conn = sqlite3.connect("database.db") #create / fetch database
c = conn.cursor() #create cursor


#commented out because it only needs to create once
#CREATE TABLE---------------------------------------------------------------------------------------
'''c.execute("""CREATE TABLE userinfo(
    username text,
    password text
    )""")
'''
#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)

pathlogin = "login.py"
argslogin = '"%s" "%s"' % (sys.executable, pathlogin)


#FUNCTIONS ---------------------------------------------------------
def hashfunc(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def signup():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    repassword = repassword_entry.get().strip()

    if len(username) < 1:
        messagebox.showerror("Error", "Username must be at least 1 character long.")
        
    elif len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long.")
        return False

    elif password != repassword:
        messagebox.showerror("Error", "Passwords do not match.")
        return False

    else: 
        hashedpw = hashfunc(password)

        conn = sqlite3.connect("database.db") #create / fetch database
        c = conn.cursor() #create cursor

        #insert into table
        c.execute("INSERT INTO userinfo VALUES (:username, :password)", 
            {
                'username': username_entry.get(),
                'password': hashedpw
            }
        )

        conn.commit() #commit changes
        conn.close() #close connection

        #clear the entry boxes
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        repassword_entry.delete(0, END)

        messagebox.showinfo("Success", "Account created successfully!")
        REGwindow.destroy()
        proc = subprocess.run(argslogin)


#FRAME---------------------------------------------------------------
frame=Frame(REGwindow, bg="#FFFFFF", padx=20, pady=20)


#WIDGETS-------------------------------------------------------------
reg_title = Label(frame, text="REGISTRATION", font=font_30, padx=0, pady=30, bg="#FFFFFF")

username_label = Label(frame, text="Username", font=font_15, pady=5, bg="#FFFFFF")
username_entry = Entry(frame, font=font_15, bg="#FFFFFF")

password_label = Label(frame, text="Password", font=font_15, pady=5, bg="#FFFFFF")
password_entry = Entry(frame, show="•", font=font_15, bg="#FFFFFF")

repassword_label = Label(frame, text="Re-enter Password", font=font_15, pady=5, bg="#FFFFFF")
repassword_entry = Entry(frame, show="•", font=font_15, bg="#FFFFFF")

#loginPage_button = Button(frame, text = "Already have an account? Login now!", font=font_15, fg= "navy", bg= "#FFFFFF" ,relief="flat")
create_button = Button(frame, text="Create Account", font=font_20, bg="#FFFFFF", borderwidth=0, padx=50, command=signup)


#PACK IT IN (OR GRID IG)----------------------------------------------
reg_title.grid(row=0, column=1, columnspan=2, sticky="ew")

username_label.grid(row=1, column=1)
username_entry.grid(row=1, column=2)

password_label.grid(row=2, column=1)
password_entry.grid(row=2, column=2)

repassword_label.grid(row=3, column=1)
repassword_entry.grid(row=3, column=2)

create_button.grid(row=4, column=1, columnspan=2)
#loginPage_button.grid(row= 5, column= 1, columnspan=2, sticky="ew")

frame.pack(side="top", expand=True)

REGwindow.mainloop()