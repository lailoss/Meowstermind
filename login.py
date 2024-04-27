from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("1200x700")
root.title("Login Page")
root.configure(bg="#E8D09C")


#FUNCTIONS ---------------------------------------------------------
"""def login():
    username="meowstermind" #link db
    password="12345" #link db
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You shall pass.")
    else:
        messagebox.showerror(title="Error", message="You shall not pass.")"""


#FRAME---------------------------------------------------------------
frame=Frame(root, bg="#FFFFFF", padx=20, pady=20)


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)


#WIDGETS-------------------------------------------------------------
login_title = Label(frame, text="LOGIN", font=font_30, padx=0, pady=30, bg="#FFFFFF")
username_label = Label(frame, text="Username", font=font_15, padx=30, pady=15, bg="#FFFFFF")
username_entry = Entry(frame, font=font_15, bg="#FFFFFF")
username_entry.get()
password_label = Label(frame, text="Password", font=font_15, padx=30, pady=15, bg="#FFFFFF")
password_entry = Entry(frame, show="•", font=font_15, bg="#FFFFFF")
password_entry.get()

register_button = Button(frame, text = "Don't have an account? Register now!", font=font_15, fg= "blue", bg= "#FFFFFF" ,relief="flat") #change to hyperlink
login_button = Button(frame, text="Login", font=font_20, bg="#FFFFFF", relief= "flat", padx=50)


#pack it in
login_title.grid(row=0, column=1, columnspan=2, sticky="ew")
username_label.grid(row=1, column=1)
username_entry.grid(row=1, column=2)
password_label.grid(row=2, column=1)
password_entry.grid(row=2, column=2)
register_button.grid(row= 3, column= 1, columnspan=2, sticky="ew")
login_button.grid(row=4, column=1, columnspan=2)

frame.pack(side="top", expand=True)


root.mainloop()