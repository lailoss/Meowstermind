from tkinter import *
from tkinter import messagebox
import login
REGwindow = Tk()
REGwindow.geometry("1200x700")
REGwindow.title("Registration")
REGwindow.configure(bg="#E8D09C")


#FUNCTIONS ---------------------------------------------------------
def register():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    repassword = repassword_entry.get().strip()
    if len(username) < 1:
        messagebox.showerror("Error", "Username must be at least 1 character long.")
    elif len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long.")
        return False
    elif password != repassword:
        messagebox.showerror("Error", "Passwords do not match.")
        return False
    else: 
        messagebox.showinfo("Success", "Account created successfully!")
        login.create_LOGwindow()
        REGwindow.withdraw()


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)


#FRAME---------------------------------------------------------------
frame=Frame(REGwindow, bg="#FFFFFF", padx=20, pady=20)


#WIDGETS-------------------------------------------------------------
register_title = Label(frame, text="REGISTRATION", font=font_30, padx=0, pady=30, bg="#FFFFFF")

username_label = Label(frame, text="Username", font=font_15, pady=5, bg="#FFFFFF")
username_entry = Entry(frame, font=font_15, bg="#FFFFFF")

password_label = Label(frame, text="Password", font=font_15, pady=5, bg="#FFFFFF")
password_entry = Entry(frame, show="•", font=font_15, bg="#FFFFFF")

repassword_label = Label(frame, text="Re-enter Password", font=font_15, pady=5, bg="#FFFFFF")
repassword_entry = Entry(frame, show="•", font=font_15, bg="#FFFFFF")

register_button = Button(frame, text = "Already have an account? Login now!", font=font_15, fg= "navy", bg= "#FFFFFF" ,relief="flat") #change to hyperlink
create_button = Button(frame, text="Create Account", font=font_20, bg="#FFFFFF", borderwidth=0, padx=50, command=register)


#BINDERS--------------------------------------------------------------


#PACK IT IN (OR GRID IG)----------------------------------------------
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

REGwindow.mainloop()