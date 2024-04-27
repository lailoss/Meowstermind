from tkinter import *
from tkinter import messagebox
import os
root = Tk()
root.geometry("1200x700")
root.title("Registration")
root.configure(bg="#E8D09C")


#FUNCTIONS ---------------------------------------------------------
def register():
    if password_entry.get() == repassword_entry.get():
        create_button.config(state=NORMAL)
        os.system("login.py")

    else:
        create_button.config(state=DISABLED)


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)


#FRAME---------------------------------------------------------------
frame=Frame(root, bg="#FFFFFF", padx=20, pady=20)


#WIDGETS-------------------------------------------------------------
register_title = Label(frame, text="REGISTRATION", font=font_30, padx=0, pady=30, bg="#FFFFFF")
username_label = Label(frame, text="Username", font=font_15, pady=5, bg="#FFFFFF")
username_entry = Entry(frame, font=font_15, bg="#FFFFFF")
username_entry.get()
password_label = Label(frame, text="Password", font=font_15, pady=5, bg="#FFFFFF")
password_entry = Entry(frame, show="•", font=font_15, bg="#FFFFFF")
repassword_label = Label(frame, text="Re-enter Password", font=font_15, pady=5, bg="#FFFFFF")
repassword_entry = Entry(frame, show="•", font=font_15, bg="#FFFFFF")
repassword_entry.get() #uuuuuuuuuuuuuuuuuuuuuu

register_button = Button(frame, text = "Alredy have an account? Login now!", font=font_15, fg= "navy", bg= "#FFFFFF" ,relief="flat") #change to hyperlink

create_button = Button(frame, text="Create Account", font=font_20, bg="#FFFFFF", borderwidth=0, padx=50, command=register)


#pack it in
register_title.grid(row=0, column=1, columnspan=2, sticky="ew")
username_label.grid(row=1, column=1)
username_entry.grid(row=1, column=2)
password_label.grid(row=2, column=1)
password_entry.grid(row=2, column=2)
repassword_label.grid(row=3, column=1)
repassword_entry.grid(row=3, column=2)
create_button.grid(row=4, column=1, columnspan=2)
register_button.grid(row= 5, column= 1, columnspan=2, sticky="ew")

frame.pack(side="top", expand=True)

root.mainloop()