from tkinter import *
import sqlite3

admin = Tk()
admin.geometry("600x600")
admin.configure(bg="#E8D09C")
admin.title("Admin Page")

#FUNCTIONS ----------------------------------------------------------

def query():
    conn = sqlite3.connect("account.db") #create / fetch database
    c = conn.cursor() #create cursor

    c.execute("SELECT *, oid FROM userinfo")
    records = c.fetchall()
    print(records)

    print_records=''
    for record in records:
        print_records += str(record[0]) + "  " + str(record[1]) + "  " + str(record[2]) + "\n"

    query_label= Label(frame, text=print_records)
    query_label.grid(row=1, column=0)

    conn.commit() #commit changes
    conn.close() #close connection


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)


#WIDGETS-------------------------------------------------------------
frame=Frame(admin, bg="#FFFFFF", padx=20, pady=20)
frame.pack(side="top", expand=True)

query = Button(frame, text="Show records", command=query)
query.grid(row=0, column=0)

admin.mainloop()