from tkinter import *
import sqlite3

admin = Tk()
admin.geometry("600x700")
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

    query_label= Label(frame, text=print_records, font=font_15, bg="#FFFFFF")
    query_label.grid(row=8, column=0, columnspan=2, pady=(20,0))

    conn.commit() #commit changes
    conn.close() #close connection


def delete():
    conn = sqlite3.connect("account.db") #create / fetch database
    c = conn.cursor() #create cursor

    #delete from record
    c.execute("DELETE from userinfo WHERE oid= " + delentry.get())

    delentry.delete(0, END) #clear entry box
    conn.commit() #commit changes
    conn.close() #close connection

'''    #clear the entry boxes
    username.delete(0, END)
    password.delete(0, END)'''


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)


#WIDGETS-------------------------------------------------------------
frame=Frame(admin, bg="#FFFFFF", padx=20, pady=20)
frame.pack(side="top", expand=True)

admin_title = Label(frame, text="ADMIN SETTINGS", font=font_30, padx=0, pady=30, bg="#FFFFFF")
admin_title.grid(row=0, column=0, columnspan=2, sticky="ew")

dellabel = Label(frame, text="ID Number", font=font_15, bg="#FFFFFF")
dellabel.grid(row=1, column=0, pady=20)

delentry = Entry(frame, font=font_15)
delentry.grid(row=1, column=1)

delbutton = Button(frame, text="Delete a record", font=font_15, bg="#FFFFFF", command=delete)
delbutton.grid(row=2, column=0, columnspan=2)

query = Button(frame, text="Show records", font=font_15, bg="#FFFFFF", command=query)
query.grid(row=7, column=0, columnspan=2, pady=10)

admin.mainloop()