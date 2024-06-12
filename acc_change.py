from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import sys

if len(sys.argv) > 1: #Ensure username is passed correctly from the command line arguments
    username = sys.argv[1]
    print(f"Username received: {username}")
else:
    print("Error: No username provided")
    sys.exit(1)
print("Username check passed")


acc_change = Tk()
acc_change.geometry("400x600")
acc_change.title("Account Info Page")

#tabs
notebook = ttk.Notebook(acc_change)
notebook.pack(expand=True, fill='both')

tab1 = Frame(notebook, bg="#99FF98")
notebook.add(tab1, text="View Your Info")

tab2 = Frame(notebook, bg="#99FF98")
notebook.add(tab2, text="Edit Your Info")


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)


#FUNCTIONS-----------------------------------------------------------
def display():
    for widget in tab1.winfo_children(): #destroy existing widgets in tab1
        widget.destroy()

    conn = sqlite3.connect("database.db")  # Create / fetch database
    c = conn.cursor()  # Create cursor

    c.execute("SELECT * FROM userinfo WHERE username=?", (username,))
    record = c.fetchone()
    print("Fetched record:", record)

    if record and len(record) == 2:
        display_username, display_password = record

        #WIDGETS-------------------------------------------------------------
        cupboard = Frame(tab1, bg="#FFFFFF", padx=20, pady=20)
        cupboard.pack(side="top", expand=True)

        acc_change_title = Label(cupboard, text="YOUR\nACCOUNT", font=font_30, padx=0, pady=20, bg="#FFFFFF")
        acc_change_title.grid(row=0, column=0, columnspan=2, sticky="ew")

        username_text = Label(cupboard, text="Username:", font=font_15, bg="#FFFFFF")
        username_text.grid(row=1, column=0, pady=(15, 0))

        username_label = Label(cupboard, text=display_username, font=font_15, bg="#FFFFFF")
        username_label.grid(row=1, column=1, pady=(15, 0))

        password_text = Label(cupboard, text="Password:", font=font_15, bg="#FFFFFF")
        password_text.grid(row=2, column=0, pady=(15, 0))

        password_label = Label(cupboard, text=display_password, font=font_15, bg="#FFFFFF")
        password_label.grid(row=2, column=1, pady=(15, 0))

    else:
        print(f"No valid user record found for the username: {username}")

    conn.commit()  # Commit changes
    conn.close()  # Close connection


def edit():
    for widget in tab2.winfo_children(): #destroy existing widgets in tab2
        widget.destroy()

    conn = sqlite3.connect("database.db") #create / fetch database
    c = conn.cursor() #create cursor

    c.execute("SELECT * FROM userinfo WHERE username=?", (username,))
    records = c.fetchone()
    print("To be edited:", records)

    #WE GOING GLOBAL YALL------------------------------------------------
    global username_entry
    global password_entry
    global repassword_entry

    #WIDGETS-------------------------------------------------------------
    cabinet=Frame(tab2, bg="#FFFFFF", padx=20, pady=20)
    cabinet.pack(side="top", expand=True)

    editor_title = Label(cabinet, text="EDIT", font=font_30, padx=0, pady=20, bg="#FFFFFF")
    editor_title.grid(row=0, column=0, columnspan=2, sticky="ew")    

    username_label = Label(cabinet, text="Username", font=font_15, pady=5, bg="#FFFFFF")
    username_label.grid(row=1, column=0)

    username_entry = Entry(cabinet, font=font_15, bg="#FFFFFF")
    username_entry.grid(row=1, column=1)

    password_label = Label(cabinet, text="Password", font=font_15, pady=5, bg="#FFFFFF")
    password_label.grid(row=2, column=0)

    password_entry = Entry(cabinet, show="•", font=font_15, bg="#FFFFFF")
    password_entry.grid(row=2, column=1)

    repassword_label = Label(cabinet, text="Re-enter Password", font=font_15, pady=5, bg="#FFFFFF")
    repassword_label.grid(row=3, column=0)

    repassword_entry = Entry(cabinet, show="•", font=font_15, bg="#FFFFFF")
    repassword_entry.grid(row=3, column=1)

    savebutton = Button(cabinet, text="Save changes", font=font_15, bg="#FFFFFF", command=save)
    savebutton.grid(row=4, column=0, columnspan=2, pady=(50,0))

    #FILL IN THE BLANK----------------------------------------------------
    #to loop through results
    #placed after widget so it works
    if records:
        username_entry.insert(0, records[0])
        password_entry.insert(0, records[1])


def save():
    newusername = username_entry.get().strip()
    newpassword = password_entry.get().strip()
    repassword = repassword_entry.get().strip()

    if len(newusername) < 1:
        messagebox.showerror("Error", "Username must be at least 1 character long.")
        
    elif len(newpassword) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long.")
        return False

    elif newpassword != repassword:
        messagebox.showerror("Error", "Passwords do not match.")
        return False

    else: 
        conn = sqlite3.connect("database.db") #create / fetch database
        c = conn.cursor() #create cursor
        global username

        #insert into table
        c.execute("""
            UPDATE userinfo
            SET username = ?, password = ?
            WHERE username = ?
        """, (newusername, newpassword, username))

        #clear the entry boxes
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        repassword_entry.delete(0, END)

        messagebox.showinfo("Success", "Account updated successfully!")

        conn.commit()
        conn.close()

        username = newusername
        display()


display() #call function in order to execute it
edit()
acc_change.mainloop()