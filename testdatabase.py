from tkinter import *
import sqlite3
root = Tk()
root.title("database")
root.geometry("500x500")


conn = sqlite3.connect("account.db") #create / fetch database
c = conn.cursor() #create cursor


#commented out because it only needs to create once
'''#CREATE TABLE----------------------------------------------------------------
c.execute("""CREATE TABLE accounts(
    username text,
    password text
    )""")
'''


#FUNCTIONS----------------------------------------------------------------------

def submit(): 
    conn = sqlite3.connect("account.db") #create / fetch database
    c = conn.cursor() #create cursor

    #insert into table
    c.execute("INSERT INTO accounts VALUES (:username, :password)", 
        {
            'username': username.get(),
            'password': password.get()
        }
    )

    conn.commit() #commit changes
    conn.close() #close connection

    #clear the entry boxes
    username.delete(0, END)
    password.delete(0, END)


def query():
    conn = sqlite3.connect("account.db") #create / fetch database
    c = conn.cursor() #create cursor

    c.execute("SELECT *, oid FROM accounts")
    records = c.fetchall()
    print(records)

    print_records=''
    for record in records:
        print_records += str(record[0]) + "  " + str(record[2]) + "\n"

    query_label= Label(root, text=print_records)
    query_label.grid(row=10, column=0, columnspan=2)

    conn.commit() #commit changes
    conn.close() #close connection


def delete():
    conn = sqlite3.connect("account.db") #create / fetch database
    c = conn.cursor() #create cursor

    #delete from record
    c.execute("DELETE from accounts WHERE oid= " + delete_box.get())

    delete_box.delete(0, END) #clear entry box
    conn.commit() #commit changes
    conn.close() #close connection

    #clear the entry boxes
    username.delete(0, END)
    password.delete(0, END)


def update():
    global editor
    conn = sqlite3.connect("account.db") #create / fetch database
    c = conn.cursor() #create cursor

    record_id = delete_box.get()

    c.execute("""UPDATE accounts SET
        username = :username,
        password = :password

        WHERE oid = :oid""",
            {
                'username': username_editor.get(),
                'password': password_editor.get(),

                'oid': record_id
            }
    ) # to replace with new info

    conn.commit() #commit changes
    conn.close() #close connection

    editor.destroy()


def edit():
    global editor
    editor = Tk()
    editor.title("Edit Record")
    editor.geometry("500x500")

    conn = sqlite3.connect("account.db") #create / fetch database
    c = conn.cursor() #create cursor

    record_id = delete_box.get()
    c.execute("SELECT * FROM accounts WHERE oid =" + record_id)
    records = c.fetchall()

    #WE GOING GLOBAL (since its used in prev func-------------
    global username_editor
    global password_editor


    #REPEAT INPUTS--------------------------------------------
    unlabel_editor = Label(editor, text="Username", pady=10)
    unlabel_editor.grid(row= 0, column= 0)

    username_editor = Entry(editor)
    username_editor.grid(row=0, column=1)

    passlabel_editor = Label(editor, text="Password", pady=10)
    passlabel_editor.grid(row=1, column= 0)

    password_editor = Entry(editor)
    password_editor.grid(row=1, column=1)

    save = Button(editor, text="Save a record", command=update)
    save.grid(row= 3, column= 0, columnspan=2, ipadx= 52)

    #LOOP THROUGH RECORDS-------------------------------------
    for record in records:
        username_editor.insert(0, record[0])
        password_editor.insert(0, record[1])


#WIDGETS & GRID--------------------------------------------------------------
unlabel = Label(root, text="Username", pady=10)
unlabel.grid(row= 0, column= 0)

username = Entry(root)
username.grid(row=0, column=1)

passlabel = Label(root, text="Password", pady=10)
passlabel.grid(row=1, column= 0)

password = Entry(root)
password.grid(row=1, column=1)

submit = Button(root, text="Submit to db", command=submit)
submit.grid(row= 3, column= 0, columnspan = 2, ipadx=50)

query = Button(root, text="Show records", command=query)
query.grid(row= 4, column= 0, columnspan = 2, ipadx=49)

delete_box = Entry(root)
delete_box.grid(row=5, column=1)

delete_label = Label(root, text="ID Number")
delete_label.grid(row=5, column=0, pady=20)

delete = Button(root, text="Delete a record", command=delete)
delete.grid(row= 6, column= 0, columnspan = 2, ipadx=45)

edit = Button(root, text="Edit a record", command=edit)
edit.grid(row= 7, column= 0, columnspan=2, ipadx= 52)

conn.commit() #commit changes
conn.close() #close connection

root.mainloop()