from tkinter import *
import sqlite3

admin = Tk()
admin.geometry("500x600")
admin.configure(bg="#99BDFA")
admin.title("Admin Page")


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20, "bold")
font_15b = ("Gill Sans MT", 15, "bold")
font_15 = ("Gill Sans MT", 15)


#FUNCTIONS ----------------------------------------------------------

def query():
    conn = sqlite3.connect("database.db") #create / fetch database
    c = conn.cursor() #create cursor

    c.execute("SELECT *, oid FROM userinfo")
    records = c.fetchall()
    print("all records fetched")

    meowers = Tk()
    meowers.geometry("400x500")
    meowers.configure(bg="#99BDFA")
    meowers.title("Meowers")


    #WIDGETS-------------------------------------------------------------
    drawer = Frame(meowers, bg="#FFFFFF", padx=20, pady=20)
    drawer.pack(side="top", expand=True)

    meowers_title = Label(drawer, text="MEOWERS", font=font_20, padx=0, pady=20, bg="#FFFFFF")
    meowers_title.grid(row=0, column=0, columnspan=2, sticky="ew")

    oidtext = Label(drawer, text="oid", font=font_15b, bg="#FFFFFF")
    oidtext.grid(row=1, column=0, padx=(15,25))

    usernametext = Label(drawer, text="  Username", font=font_15b, bg="#FFFFFF")
    usernametext.grid(row=1, column=1, padx=(30,15))

    cupboard = Frame(drawer, bg="#FFFFFF")
    cupboard.grid(row=2, column=0, columnspan=2)

    max_username_length = max(len(record[0]) for record in records)

    record_label = Text(cupboard, font=font_15, bg="#FFFFFF", width=max_username_length + 17, height=10) #text so that we can add scrollbar
    record_label.pack(side="left", fill="both", expand=True)
    
    for record in records:
        betteroid = f"{record[3]:02}"
        record_label.insert("end", "     " + betteroid + "\t\t" + str(record[0]) + "\n")

    record_label.config(state="disabled") #makes it read-only

    scrollbar = Scrollbar(cupboard, orient="vertical")
    scrollbar.pack(side="right", fill="y")
    record_label.config(yscrollcommand=scrollbar.set) #scrollbar added here
    scrollbar.config(command=record_label.yview) #verticalized the scrollbar based on record_label


    conn.commit() #commit changes
    conn.close() #close connection


def delete():
    conn = sqlite3.connect("database.db") #create / fetch database
    c = conn.cursor() #create cursor

    #delete from record
    c.execute("DELETE from userinfo WHERE oid= " + identry.get())

    identry.delete(0, END) #clear entry box
    conn.commit() #commit changes
    conn.close() #close connection


#WIDGETS-------------------------------------------------------------
frame=Frame(admin, bg="#FFFFFF", padx=20, pady=20)
frame.pack(side="top", expand=True)

admin_title = Label(frame, text="ADMIN SETTINGS", font=font_30, padx=0, pady=30, bg="#FFFFFF")
admin_title.grid(row=0, column=0, columnspan=2, sticky="ew")

idlabel = Label(frame, text="ID Number", font=font_15, bg="#FFFFFF")
idlabel.grid(row=1, column=0, pady=20)

identry = Entry(frame, font=font_15)
identry.grid(row=1, column=1)

delbutton = Button(frame, text="Delete record", font=font_15, fg="red", bg="#FFFFFF", relief="flat", command=delete)
delbutton.grid(row=3, column=0, columnspan=2)

querybutton = Button(frame, text="Show records", font=font_15, bg="#FFFFFF", command=query)
querybutton.grid(row=4, column=0, pady=(50,0), columnspan=2)

admin.mainloop()