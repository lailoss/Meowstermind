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
#fonts
font_30 = ("Gill Sans MT", 30, "bold")
font_15 = ("Gill Sans MT", 15)

#quotes pictures
mascotpic = PhotoImage(file="picreg.png")
qtitle = PhotoImage(file="./quotes/title/t1.png")

images = [f"./quotes/content/wp{i}.png" for i in range(1, 11)]
images_dict = {i:ImageTk.PhotoImage(Image.open(image)) for i, image in enumerate(images)}

#icon pictures
todo_pic = PhotoImage(file="./icons/icon1.png")
pomo_pic = PhotoImage(file="./icons/icon2.png")
scratch_pic = PhotoImage(file="./icons/icon3.png")
music_pic = PhotoImage(file="./icons/icon4.png")
flash_pic = PhotoImage(file="./icons/icon5.png")

#paths
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

def quote(quotepic, index):
    random_index = random.randint(0, len(images) - 1)  #Generate a random index
    quotepic.config(image=images_dict[random_index]) 
    root.after(10000, lambda idx=random_index: quote(quotepic, idx))

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
midframe = Frame(root, bg="#FFFFFF", borderwidth=0)
midframe.pack(expand= TRUE)

midframe1 = Frame(midframe, bg="#FFFFFF")
midframe1.grid(row=0, column=0)

midframe2 = Frame(midframe, bg="#FFFFFF")
midframe2.grid(row=0, column=1)

'''mascot = Label(midframe1, image=mascotpic)
mascot.grid(row=0, column=0, rowspan=2)'''

quotetitle = Label(midframe2, bg="#FFFFFF", font=font_15, image=qtitle)
quotetitle.grid(row=0, column=0, pady=(5))

quotepic = Label(midframe2)
quotepic.grid(row=1, column=0, pady=5)
quote(quotepic, 0)

#footer
botframe = Frame(root, bg="#FFFFFF", padx=20, pady=10, borderwidth=0)
botframe.pack(side="bottom")

todo_button = Button(botframe, image=todo_pic, bg= "#FFFFFF", borderwidth=0, command= redirect_todo)
todo_button.grid(row= 1, column= 1, padx=10)

pomodoro_button = Button(botframe, image=pomo_pic, bg= "#FFFFFF", borderwidth=0, command= redirect_pomo)
pomodoro_button.grid(row= 1, column= 2, padx=10)

scratch_button = Button(botframe, image=scratch_pic, bg= "#FFFFFF", borderwidth=0, command= redirect_scratch)
scratch_button.grid(row= 1, column= 3, padx=10)

music_button = Button(botframe, image=music_pic, bg="#FFFFFF", borderwidth=0, command= redirect_music)
music_button.grid(row= 1, column= 4, padx=10)

flash_button = Button(botframe, image=flash_pic, bg= "#FFFFFF", borderwidth=0, command= redirect_flash)
flash_button.grid(row= 1, column= 5, padx=10)


root.mainloop()