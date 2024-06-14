from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import sys
import bcrypt

if len(sys.argv) > 1: #Ensure username is passed correctly from the command line arguments
    username = sys.argv[1]
    print(f"Username received: {username}")
else:
    print("Error: No username provided")
    sys.exit(1)
print("Username check passed")


acc_change = Tk()
acc_change.geometry("500x650")
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
    global currpw_entry
    global newpw_entry
    global repassword_entry

    #WIDGETS-------------------------------------------------------------
    cabinet=Frame(acc_change, bg="#FFFFFF", padx=20, pady=20)
    cabinet.pack(side="top", expand=True)

    editor_title = Label(cabinet, text="EDIT ACCOUNT\nDETAILS", font=font_30, padx=0, pady=20, bg="#FFFFFF")
    editor_title.grid(row=0, column=0, columnspan=2, sticky="ew")    

    username_label = Label(cabinet, text="Username", font=font_15, pady=5, bg="#FFFFFF")
    username_label.grid(row=1, column=0, pady=5)

    username_entry = Entry(cabinet, font=font_15, bg="#FFFFFF")
    username_entry.grid(row=1, column=1)

    currpw_label = Label(cabinet, text="Current Password", font=font_15, pady=5, bg="#FFFFFF")
    currpw_label.grid(row=2, column=0, pady=5, padx=5)

    currpw_entry = Entry(cabinet, show="•", font=font_15, bg="#FFFFFF")
    currpw_entry.grid(row=2, column=1)

    newpw_label = Label(cabinet, text="New Password", font=font_15, pady=5, bg="#FFFFFF")
    newpw_label.grid(row=3, column=0, pady=5)

    newpw_entry = Entry(cabinet, show="•", font=font_15, bg="#FFFFFF")
    newpw_entry.grid(row=3, column=1)

    repassword_label = Label(cabinet, text="Re-enter New\nPassword", font=font_15, pady=5, bg="#FFFFFF")
    repassword_label.grid(row=4, column=0, pady=5)

    repassword_entry = Entry(cabinet, show="•", font=font_15, bg="#FFFFFF")
    repassword_entry.grid(row=4, column=1)

    savebutton = Button(cabinet, text="Save Changes", font=font_15, bg="#FFFFFF", command=save)
    savebutton.grid(row=5, column=0, columnspan=2, pady=(50,0))

    #FILL IN THE BLANK----------------------------------------------------
    #to loop through results
    #placed after widget so it works
    if records:
        username_entry.insert(0, records[0])


def save():
    newun = username_entry.get().strip()
    currpw = currpw_entry.get().strip()
    newpw = newpw_entry.get().strip()
    repassword = repassword_entry.get().strip()

    conn = sqlite3.connect("database.db")  # create / fetch database
    c = conn.cursor()  # create cursor

    c.execute("SELECT password FROM userinfo WHERE username=?", (username,))
    user = c.fetchone()

    if not user:
        messagebox.showerror("Error", "User not found.")
        return

    hashedpw = user[0]

    # Verify current password
    if not bcrypt.checkpw(currpw.encode(), hashedpw.encode()):
        messagebox.showerror("Error", "Incorrect current password.")
        return

    if len(newun) < 1:
        messagebox.showerror("Error", "Username must be at least 1 character long.")
        return
        
    elif len(newpw) < 8:
        messagebox.showerror("Error", "New password must be at least 8 characters long.")
        return False

    elif newpw != repassword:
        messagebox.showerror("Error", " New passwords do not match.")
        return False
    
    try:
        new_hashedpw = bcrypt.hashpw(newpw.encode(), bcrypt.gensalt()).decode()
        c.execute("UPDATE userinfo SET password = ? WHERE username = ?", (new_hashedpw, username))
        conn.commit()
        messagebox.showinfo("Success", "Account details updated successfully!")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        conn.close()


        # Clear entry boxes
        currpw_entry.delete(0, END)
        newpw_entry.delete(0, END)
        repassword_entry.delete(0, END)

        messagebox.showinfo("Success", "Account details updated successfully!")

edit()
acc_change.mainloop()


"""    else: 
        new_hashedpw = bcrypt.hashpw(newpw.encode(), bcrypt.gensalt()).decode()
        c.execute("UPDATE userinfo SET password = ? WHERE username = ?", (new_hashedpw, username))
        conn.commit()
        conn.close()"""
