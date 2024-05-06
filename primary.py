from tkinter import *
'''import register
import login'''

primary = Tk()
primary.geometry("1200x700")
primary.configure(bg="#E8D09C")
primary.title("Welcome!")


#FUNCTIONS ----------------------------------------------------------

def redirect_l():
    import login
    create_LOGwindow()

def redirect_r():
    import register
    create_REGwindow()


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)


#WIDGETS-------------------------------------------------------------

#weights
primary.grid_columnconfigure(0, weight=1) #helps with centering , by column
primary.grid_columnconfigure(1, weight=1)
#primary.grid_rowconfigure(0, weight=1) #helps with centering , by row


title = Label(primary, text="Welcome!", font=font_30, pady=50, bg="#E8D09C")
title.grid(row =0, column=0, columnspan=2, sticky="ew")

frame1 = Frame(primary, padx=20, pady=20)
frame1.grid(row=1, column=0)

reglabel = Label(frame1, text="Are you a new member? Register here!", font=font_15, padx=10, pady=20)
reglabel.grid(row=0, column=0)

regbutton = Button(frame1, text= "Register", font=font_20, padx=10, pady=10, command=redirect_r)
regbutton.grid(row=1, column=0)

frame2 = Frame(primary, padx=20, pady=20)
frame2.grid(row=1, column=1)

loglabel = Label(frame2, text="Already have an account? Welcome back!", font=font_15, padx=10, pady=20)
loglabel.grid(row=0, column=0)

logbutton = Button(frame2, text= "Login", font=font_20, padx=10, pady=10, command=redirect_l)
logbutton.grid(row=1, column=0)


primary.mainloop()