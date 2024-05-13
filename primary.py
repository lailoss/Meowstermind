from tkinter import *

primary = Tk()
primary.geometry("1200x700")
primary.configure(bg="#E8D09C")
primary.title("Welcome!")


#FUNCTIONS ----------------------------------------------------------

def redirect_l():
    primary.destroy()
    import login
    login.create_LOGwindow()

def redirect_r():
    primary.destroy()
    import register
    register.create_REGwindow()


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)


#WIDGETS-------------------------------------------------------------

#weights
primary.grid_columnconfigure(0, weight=1) #helps with centering , by column
primary.grid_columnconfigure(1, weight=1)
#primary.grid_rowconfigure(0, weight=1) #helps with centering , by row


title = Label(primary, text="W E L C O M E", font=font_30, pady=50, bg="#E8D09C")
title.grid(row =0, column=0, columnspan=2, sticky="ew")

frame1 = Frame(primary, padx=20, pady=20, bg="#FFFFFF")
frame1.grid(row=1, column=0)

reglabel = Label(frame1, text="Are you a new member?\n", font=font_20, padx=10, pady=20, bg="#FFFFFF")
reglabel.grid(row=0, column=0)

picreg = PhotoImage(file="picreg.png")
picreglabel = Label(frame1,image=picreg, pady=5, bg="#FFFFFF")
picreglabel.grid(row=1, column=0)

regbutton = Button(frame1, text= "Register here!", font=font_20, padx=10, bg="#FFFFFF", borderwidth=1, command=redirect_r)
regbutton.grid(row=2, column=0)

frame2 = Frame(primary, padx=20, pady=20, bg="#FFFFFF")
frame2.grid(row=1, column=1)

loglabel = Label(frame2, text="Already have an account?\nWelcome back!", font=font_20, padx=10, pady=20, bg="#FFFFFF")
loglabel.grid(row=0, column=0)

piclog = PhotoImage(file="piclog.png")
picloglabel = Label(frame2,image=piclog, pady=5, bg="#FFFFFF")
picloglabel.grid(row=1, column=0)

logbutton = Button(frame2, text= "Login", font=font_20, padx=10, bg="#FFFFFF", borderwidth=1, command=redirect_l)
logbutton.grid(row=2, column=0, ipadx=50)


primary.mainloop()