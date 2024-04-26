from tkinter import *
root = Tk()
root.geometry("1200x700")
root.title("Home Screen")
root.configure(bg="#E8D09C")

#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_15 = ("Gill Sans MT", 15)


#WIDGETS-------------------------------------------------------------
pomodoro_button = Button(root, text="time", bg= "#FFFFFF")
music_button = Button(root, text="song", bg="#FFFFFF")

#PACK IT IN----------------------------------------------------------
pomodoro_button.grid(row= 1, column= 1)
music_button.grid(row= 1, column= 2)

root.mainloop()