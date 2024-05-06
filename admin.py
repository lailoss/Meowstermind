from tkinter import *

admin = Tk()
admin.geometry("600x600")
admin.configure(bg="#E8D09C")
admin.title("Admin Page")

#FUNCTIONS ----------------------------------------------------------



#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_20 = ("Gill Sans MT", 20)
font_15 = ("Gill Sans MT", 15)


#WIDGETS-------------------------------------------------------------
frame=Frame(admin, bg="#FFFFFF", padx=20, pady=20)
frame.pack(side="top", expand=True)

admin.mainloop()