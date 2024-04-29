from tkinter import *
import sqlite3
root = Tk()
root.title("database")
root.geometry("500x500")


conn = sqlite3.connect("account.db") #create / fetch database
c = conn.cursor() #create cursor

#CREATE TABLE------------------------------------------------------
c.execute("""CREATE TABLE accounts(
    username text,
    password text
    )""")


#WIDGETS & GRID----------------------------------------------------
unlabel = Label(root, text="Username")
unlabel.grid(row= 0, column= 0)

username = Entry(root, width=30)
username.grid(row=0, column=1, padx=20)

passlabel = Label(root, text="Password")
passlabel.grid(row=1, column= 0)

password = Entry(root, width=30)
password.grid(row=1, column=1, padx=30)


#COMMIT CHANGES----------------------------------------------------
conn.commit()


conn.close() #close connection
root.mainloop()