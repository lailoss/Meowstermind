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
acc_change.configure(bg="#99FF98")
acc_change.title("Account Info Page")


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)


#FUNCTIONS-----------------------------------------------------------
def edit():
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
    cabinet=Frame(acc_change, bg="#FFFFFF", padx=20, pady=20)
    cabinet.pack(side="top", expand=True)

    editor_title = Label(cabinet, text="EDIT ACCOUNT\nDETAILS", font=font_30, padx=0, pady=20, bg="#FFFFFF")
    editor_title.grid(row=0, column=0, columnspan=2, sticky="ew")    

    username_label = Label(cabinet, text="Username", font=font_15, pady=5, bg="#FFFFFF")
    username_label.grid(row=1, column=0)

    username_entry = Entry(cabinet, font=font_15, bg="#FFFFFF")
    username_entry.grid(row=1, column=1)

    password_label = Label(cabinet, text="Password", font=font_15, pady=5, bg="#FFFFFF")
    password_label.grid(row=2, column=0)

    password_entry = Entry(cabinet, show="•", font=font_15, bg="#FFFFFF")
    password_entry.grid(row=2, column=1)

    repassword_label = Label(cabinet, text="Re-enter\nPassword", font=font_15, pady=5, bg="#FFFFFF")
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


edit()
acc_change.mainloop()