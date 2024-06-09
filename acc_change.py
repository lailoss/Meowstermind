"""from tkinter import *
import sqlite3
import sys
print(sys.argv)
# Ensure username is passed correctly from the command line arguments
if len(sys.argv) > 1:
    username = sys.argv[1]
    print(f"Username received: {username}")
else:
    print("Error: No username provided")
    sys.exit(1)

# Initialize the main window
acc_change = Tk()
acc_change.geometry("400x600")
acc_change.configure(bg="#99BDFA")
acc_change.title("Account Info Page")

# Parameters
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)

# Function to display user information
def display():
    conn = sqlite3.connect("database.db")  # Create / fetch database
    c = conn.cursor()  # Create cursor

    # Correct SQL query with proper parameter passing
    c.execute("SELECT * FROM userinfo WHERE username=?", (username,))
    record = c.fetchone()
    print("Fetched record:", record)

    if record and len(record) == 2:
        display_username, display_password = record

        # Widgets
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

# Call the display function to show the account info window
display()

acc_change.mainloop()
"""

from tkinter import *
import sqlite3
import sys

print("Script started")
print(f"Received arguments: {sys.argv}")

# Ensure username is passed correctly from the command line arguments

if len(sys.argv) > 1:
    username = sys.argv[1]
    print(f"Username received: {username}")
else:
    print("Error: No username provided")
    sys.exit(1)

print("Username check passed")

# Initialize the main window
acc_change = Tk()
acc_change.geometry("400x600")
acc_change.configure(bg="#99BDFA")
acc_change.title("Account Info Page")

print("Main window initialized")

# Parameters
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)

print("Fonts defined")

# Function to display user information
def display():
    print("Display function called")
    conn = sqlite3.connect("database.db")  # Create / fetch database
    c = conn.cursor()  # Create cursor

    print("Database connection established")

    # Correct SQL query with proper parameter passing
    c.execute("SELECT * FROM userinfo WHERE username=?", (username,))
    record = c.fetchone()
    print("Fetched record:", record)

    if record and len(record) == 2:
        display_username, display_password = record

        print("Record found, creating widgets")

        # Widgets
        frame = Frame(acc_change, bg="#FFFFFF", padx=20, pady=20)
        frame.pack(side="top", expand=True)

        acc_change_title = Label(frame, text="YOUR ACCOUNT", font=font_30, padx=0, pady=20, bg="#FFFFFF")
        acc_change_title.grid(row=0, column=0, columnspan=2, sticky="ew")

        print("Title label created")

        username_text = Label(frame, text="Username:", font=font_15, bg="#FFFFFF")
        username_text.grid(row=1, column=0, pady=(15, 0))

        print("Username text label created")

        username_label = Label(frame, text=display_username, font=font_15, bg="#FFFFFF")
        username_label.grid(row=1, column=1, pady=(15, 0))

        print("Username label created")

        password_text = Label(frame, text="Password:", font=font_15, bg="#FFFFFF")
        password_text.grid(row=2, column=0, pady=(15, 0))

        print("Password text label created")

        password_label = Label(frame, text=display_password, font=font_15, bg="#FFFFFF")
        password_label.grid(row=2, column=1, pady=(15, 0))

        print("Password label created")

    else:
        print(f"No valid user record found for the username: {username}")

    print("Widgets created")

    conn.commit()  # Commit changes
    conn.close()  # Close connection

    print("Database connection closed")

# Call the display function to show the account info window
print("Calling display function")
display()

print("Main loop started")
acc_change.mainloop()