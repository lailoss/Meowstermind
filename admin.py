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
    print(records)

    meowmbers = Tk()
    meowmbers.geometry("400x500")
    meowmbers.configure(bg="#99BDFA")
    meowmbers.title("Meowers")

    oid_list = []
    userName_list = []

    for record in records:
        oid_list.append(str(record[2]))
        userName_list.append(str(record[0]))

    oid = "\n".join(oid_list)
    userName= "\n".join(userName_list)

    #WIDGETS-------------------------------------------------------------
    drawer = Frame(meowmbers, bg="#FFFFFF", padx=20, pady=20)
    drawer.pack(side="top", expand=True)

    meowmbers_title = Label(drawer, text="MEOWERS", font=font_20, padx=0, pady=20, bg="#FFFFFF")
    meowmbers_title.grid(row=0, column=0, columnspan=2, sticky="ew")

    oidtext = Label(drawer, text="oid", font=font_15b, bg="#FFFFFF")
    oidtext.grid(row=1, column=0, padx=25)

    userNametext = Label(drawer, text="Username", font=font_15b, bg="#FFFFFF")
    userNametext.grid(row=1, column=1, padx=25)

    oid_label = Label(drawer, text=oid, font=font_15, bg="#FFFFFF")
    oid_label.grid(row=2, column=0, pady=(5,0))

    userName_label = Label(drawer, text=userName, font=font_15, bg="#FFFFFF")
    userName_label.grid(row=2, column=1, pady=(5,0))

    #scrollbar
    canvas = Canvas(drawer, bg="#FFFFFF")
    canvas.grid(row=0, column=2, rowspan=3)

    scrollbar = Scrollbar(drawer, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=2, rowspan=3)

    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)


    conn.commit() #commit changes
    conn.close() #close connection


'''def save(): #SOON TO BE REMOVED
    conn = sqlite3.connect("database.db") #create / fetch database
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
    editor.destroy()'''


'''def edit(): #SOON TO BE REMOVED

    global editor
    editor = Tk()
    editor.geometry("400x500")
    editor.configure(bg="#99BDFA")
    editor.title("Editor") 

    conn = sqlite3.connect("database.db") #create / fetch database
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
'''

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

'''editbutton = Button(frame, text="Edit record", font=font_15, bg="#FFFFFF", relief="flat", command=edit)
editbutton.grid(row=2, column=0, columnspan=2)'''

delbutton = Button(frame, text="Delete record", font=font_15, fg="red", bg="#FFFFFF", relief="flat", command=delete)
delbutton.grid(row=3, column=0, columnspan=2)

querybutton = Button(frame, text="Show records", font=font_15, bg="#FFFFFF", command=query)
querybutton.grid(row=4, column=0, pady=(50,0), columnspan=2)

admin.mainloop()