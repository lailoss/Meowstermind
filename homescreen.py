from tkinter import *
import customtkinter
root = Tk()
root.geometry("1200x700")
root.title("Home Screen")
root.configure(bg="#E8D09C")
root.resizable(False, False)

#BACKGROUND----------------------------------------------------------


#FUNCTIONS-----------------------------------------------------------
def open_music():
    return


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_15 = ("Gill Sans MT", 15)


#FRAME---------------------------------------------------------------
frame=Frame(root, bg="#FFFFFF", padx=20, pady=20)

#WIDGETS-------------------------------------------------------------
pomodoro_button = Button(frame, text="time", bg= "#FFFFFF")
music_button = Button(frame, text="song", bg="#FFFFFF")

#PACK IT IN----------------------------------------------------------
frame.pack(side="bottom")
pomodoro_button.grid(row= 1, column= 1)
music_button.grid(row= 1, column= 2)

root.mainloop()