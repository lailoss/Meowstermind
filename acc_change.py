from tkinter import *
import sqlite3
import sys


if len(sys.argv) > 1: #Ensure username is passed correctly from the command line arguments
    username = sys.argv[1]
    print(f"Username received: {username}")
else:
    print("Error: No username provided")
    sys.exit(1)
print("Username check passed")


acc_change = Tk()
acc_change.geometry("600x700")
acc_change.configure(bg="#99BDFA")
acc_change.title("Account Info Page")


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)


#FUNCTIONS-----------------------------------------------------------
def display():
    conn = sqlite3.connect("database.db")  # Create / fetch database
    c = conn.cursor()  # Create cursor

    c.execute("SELECT * FROM userinfo WHERE username=?", (username,))
    record = c.fetchone()
    print("Fetched record:", record)

    if record and len(record) == 2:
        display_username, display_password = record

        #WIDGETS-------------------------------------------------------------
        frame = Frame(acc_change, bg="#FFFFFF", padx=20, pady=20)
        frame.pack(side="top", expand=True)

        acc_change_title = Label(frame, text="YOUR ACCOUNT", font=font_30, padx=0, pady=20, bg="#FFFFFF")
        acc_change_title.grid(row=0, column=0, columnspan=2, sticky="ew")

        username_text = Label(frame, text="Username:", font=font_15, bg="#FFFFFF")
        username_text.grid(row=1, column=0, pady=(15, 0))

        username_label = Label(frame, text=display_username, font=font_15, bg="#FFFFFF")
        username_label.grid(row=1, column=1, pady=(15, 0))

        password_text = Label(frame, text="Password:", font=font_15, bg="#FFFFFF")
        password_text.grid(row=2, column=0, pady=(15, 0))

        password_label = Label(frame, text=display_password, font=font_15, bg="#FFFFFF")
        password_label.grid(row=2, column=1, pady=(15, 0))

    else:
        print(f"No valid user record found for the username: {username}")

    conn.commit()  # Commit changes
    conn.close()  # Close connection


display() #call display function in order to execute it
acc_change.mainloop()