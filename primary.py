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

frame1 = Frame(primary, padx=20, pady=20, bg="#000A00")
frame1.grid(row=1, column=0)

regbutton = Button(frame1, text= "register", font=font_20, padx=10, pady=10, command=redirect_r)
regbutton.grid(row=0, column=0)

frame2 = Frame(primary, padx=20, pady=20)
frame2.grid(row=1, column=1)

logbutton = Button(frame2, text= "login", font=font_20, padx=10, pady=10, command=redirect_l)
logbutton.grid(row=0, column=0)


primary.mainloop()