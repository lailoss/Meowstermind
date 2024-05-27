from tkinter import *
from PIL import Image, ImageTk
import random
import subprocess
import sys
root = Tk()
root.geometry("1200x700")
root.title("Home Screen")
root.configure(bg="#E8D09C")
root.resizable(False, False)



#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_15 = ("Gill Sans MT", 15)

#icon pictures
todo_pic = PhotoImage(file="./icons/icon1.png")
pomo_pic = PhotoImage(file="./icons/icon2.png")
scratch_pic = PhotoImage(file="./icons/icon3.png")
music_pic = PhotoImage(file="./icons/icon4.png")
flash_pic = PhotoImage(file="./icons/icon5.png")

#quotes pictures
mascotpic = PhotoImage(file="picreg.png")
trial = PhotoImage(file="piclog.png")

pathtodo = "Meowtodo.py"
argstodo = '"%s" "%s"' % (sys.executable, pathtodo)

pathpomo = "pomodoro.py"
argspomo = '"%s" "%s"' % (sys.executable, pathpomo)

pathmusic = "Meowmusic.py"
argsmusic = '"%s" "%s"' % (sys.executable, pathmusic)

pathscratch = "scratchpadv2.py"
argsscratch = '"%s" "%s"' % (sys.executable, pathscratch)

pathflash = "Meowflashcard.py"
argsflash = '"%s" "%s"' % (sys.executable, pathflash)


#FUNCTIONS-----------------------------------------------------------

def redirect_todo():
    proc = subprocess.run(argstodo)

def redirect_music():
    proc = subprocess.run(argsmusic)

def redirect_pomo():
    proc = subprocess.run(argspomo)

def redirect_scratch():
    proc = subprocess.run(argsscratch)

def redirect_flash():
    proc = subprocess.run(argsflash)


#WIDGETS and PACKING-------------------------------------------------

#middle
midframe = Frame(root, bg="#FFFFFF", padx=20, pady=10, borderwidth=0)
midframe.pack()

mascot = Label(midframe, image=mascotpic)
mascot.grid(row=0, column=0, rowspan=2)

quotetitle = Label(midframe, bg="#FFFFFF", font=font_15, text="Wisdom Purrs")
quotetitle.grid(row=0, column=1)

quotepic = Label(midframe, image=trial)
quotepic.grid(row=1, column=1)

#footer
botframe = Frame(root, bg="#FFFFFF", padx=20, pady=10, borderwidth=0)
botframe.pack(side="bottom")

todo_button = Button(botframe, image=todo_pic, bg= "#FFFFFF", borderwidth=0, command= redirect_todo)
todo_button.grid(row= 1, column= 1)

pomodoro_button = Button(botframe, image=pomo_pic, bg= "#FFFFFF", borderwidth=0, command= redirect_pomo)
pomodoro_button.grid(row= 1, column= 2)

scratch_button = Button(botframe, image=scratch_pic, bg= "#FFFFFF", borderwidth=0, command= redirect_scratch)
scratch_button.grid(row= 1, column= 3)

music_button = Button(botframe, image=music_pic, bg="#FFFFFF", borderwidth=0, command= redirect_music)
music_button.grid(row= 1, column= 4)

flash_button = Button(botframe, image=flash_pic, bg= "#FFFFFF", borderwidth=0, command= redirect_flash)
flash_button.grid(row= 1, column= 5)


root.mainloop()