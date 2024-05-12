from tkinter import *
import sqlite3

admin = Tk()
admin.geometry("600x700")
admin.configure(bg="#99BDFA")
admin.title("Admin Page")


#FUNCTIONS ----------------------------------------------------------

def query():
    conn = sqlite3.connect("account.db") #create / fetch database
    c = conn.cursor() #create cursor

    c.execute("SELECT *, oid FROM userinfo")
    records = c.fetchall()
    print(records)

    meowmbers = Tk()
    meowmbers.geometry("400x500")
    meowmbers.configure(bg="#99BDFA")
    meowmbers.title("Meowers")

    print_records=''
    for record in records:
        print_records += str(record[0]) + "  " + str(record[1]) + "  " + str(record[2]) + "\n"

    #WIDGETS-------------------------------------------------------------
    drawer=Frame(meowmbers, bg="#FFFFFF", padx=20, pady=20)
    drawer.pack(side="top", expand=True)

    meowmbers_title = Label(drawer, text="MEOWERS", font=font_20, padx=0, pady=20, bg="#FFFFFF")
    meowmbers_title.grid(row=0, column=0, columnspan=2, sticky="ew")

    query_label= Label(drawer, text=print_records, font=font_15, bg="#FFFFFF")
    query_label.grid(row=1, column=0, pady=(15,0))

    conn.commit() #commit changes
    conn.close() #close connection


def save():
    conn = sqlite3.connect("account.db") #create / fetch database
    c = conn.cursor() #create cursor

    idnum = identry.get()
    c.execute(""" UPDATE userinfo SET
              username = :username,
              password = :password

              WHERE oid = :oid""",
              {'username' : username_entry.get(),
               'password' : password_entry.get(),
               'oid' : idnum
              })

    conn.commit() #commit changes
    conn.close() #close connection
    editor.destroy()


def edit():

    global editor
    editor = Tk()
    editor.geometry("400x500")
    editor.configure(bg="#99BDFA")
    editor.title("Editor") 

    conn = sqlite3.connect("account.db") #create / fetch database
    c = conn.cursor() #create cursor

    idnum = identry.get()
    c.execute("SELECT * FROM userinfo WHERE oid = " + idnum)
    records = c.fetchall()
    print(records)

    #WE GOING GLOBAL YALL------------------------------------------------
    global username_entry
    global password_entry

    #WIDGETS-------------------------------------------------------------
    cabinet=Frame(editor, bg="#FFFFFF", padx=20, pady=20)
    cabinet.pack(side="top", expand=True)

    editor_title = Label(cabinet, text="EDIT", font=font_20, padx=0, pady=20, bg="#FFFFFF")
    editor_title.grid(row=0, column=0, columnspan=2, sticky="ew")    

    username_label = Label(cabinet, text="Username", font=font_15, pady=5, bg="#FFFFFF")
    username_label.grid(row=1, column=0)

    username_entry = Entry(cabinet, font=font_15, bg="#FFFFFF")
    username_entry.grid(row=1, column=1)

    password_label = Label(cabinet, text="Password", font=font_15, pady=5, bg="#FFFFFF")
    password_label.grid(row=2, column=0)

    password_entry = Entry(cabinet, show="•", font=font_15, bg="#FFFFFF")
    password_entry.grid(row=2, column=1)

    savebutton = Button(cabinet, text="Save changes", font=font_15, bg="#FFFFFF", command=save)
    savebutton.grid(row=4, column=0, columnspan=2, pady=(50,0))

    #FILL IN THE BLANK----------------------------------------------------
    #to loop through results
    #placed after widget so it works
    for record in records:
        username_entry.insert(0, record[0])
        password_entry.insert(0, record[1])


def delete():
    conn = sqlite3.connect("account.db") #create / fetch database
    c = conn.cursor() #create cursor

    #delete from record
    c.execute("DELETE from userinfo WHERE oid= " + identry.get())

    identry.delete(0, END) #clear entry box
    conn.commit() #commit changes
    conn.close() #close connection

'''    #clear the entry boxes
    username.delete(0, END)
    password.delete(0, END)'''


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20, "bold")
font_15 = ("Gill Sans MT", 15)


#WIDGETS-------------------------------------------------------------
frame=Frame(admin, bg="#FFFFFF", padx=20, pady=20)
frame.pack(side="top", expand=True)

admin_title = Label(frame, text="ADMIN SETTINGS", font=font_30, padx=0, pady=30, bg="#FFFFFF")
admin_title.grid(row=0, column=0, columnspan=2, sticky="ew")

idlabel = Label(frame, text="ID Number", font=font_15, bg="#FFFFFF")
idlabel.grid(row=1, column=0, pady=20)

identry = Entry(frame, font=font_15)
identry.grid(row=1, column=1)

editbutton = Button(frame, text="Edit record", font=font_15, bg="#FFFFFF", relief="flat", command=edit)
editbutton.grid(row=2, column=0, columnspan=2)

delbutton = Button(frame, text="Delete record", font=font_15, fg="red", bg="#FFFFFF", relief="flat", command=delete)
delbutton.grid(row=3, column=0, columnspan=2)

querybutton = Button(frame, text="Show records", font=font_15, bg="#FFFFFF", command=query)
querybutton.grid(row=4, column=0, pady=(50,0), columnspan=2)

admin.mainloop()