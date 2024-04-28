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


#COMMIT CHANGES----------------------------------------------------
conn.commit()


conn.close() #close connection
root.mainloop()