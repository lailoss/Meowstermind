from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import random
import subprocess
import sys
import sqlite3
import os 

# Get the username from the command line arguments
username = sys.argv[1]

conn = sqlite3.connect('database.db')
c = conn.cursor()

root = Tk()
root.geometry("1200x700")
root.title("Home Screen")
root.configure(bg="#E8D09C")
root.resizable(False, False)


#PARAMETER-----------------------------------------------------------
#fonts
font_20 = ("Gill Sans MT", 20, "bold")
font_15 = ("Gill Sans MT", 15, "bold")

#topframe pictures
info_pic = PhotoImage(file="./icons/iconinfo.png")
acc_pic = PhotoImage(file="./icons/iconacc.png")
rewards_pic = PhotoImage(file="./icons/iconrewards.png")

#midframe pictures
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


#path
pathinfo = "info.py"
argsinfo = '"%s" "%s"' % (sys.executable, pathinfo)



#FUNCTIONS-----------------------------------------------------------

#topframe
def redirect_info():
    proc = subprocess.run(argsinfo)

def redirect_acc(username):
    command_acc = [sys.executable, "acc_change.py", username]
    print(f"Redirecting to acc_change.py with command: {command_acc}")
    proc = subprocess.run(command_acc)

def date_time():
    daydate = datetime.now().strftime('%a , %d %B %Y')
    daydatelabel.config(text=daydate)

    clock = datetime.now().strftime('%H:%M:%S')
    clocklabel.config(text=clock)

    root.after(1000, date_time)

#background

c.execute("SELECT background FROM timer WHERE username=? ORDER BY id DESC LIMIT 1", (username,))
current_background_result = c.fetchone()
current_background = current_background_result[0] if current_background_result else 'default'
backgrounds = {
    'default': PhotoImage(file='./backgrounds/default.png'),
    'bedroom': PhotoImage(file='./backgrounds/bedroom.png'),
    'cafe': PhotoImage(file='./backgrounds/cafe.png'),
    'meadow': PhotoImage(file='./backgrounds/meadow.png')
}
bg_image = backgrounds.get(current_background, backgrounds['default'])
bg_label = Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
def update_background(bg_name):
    global bg_image
    bg_image = backgrounds[bg_name]
    bg_label.config(image=bg_image)
    c.execute("UPDATE timer SET background=? WHERE username=?", (bg_name, username))
    conn.commit()
    
def load_background():
    if os.path.exists("current_background.txt"):
        with open("current_background.txt", "r") as f:
            bg_name = f.read().strip()
            return backgrounds.get(bg_name, backgrounds['default'])
    else:
        return backgrounds.get(current_background(), backgrounds['default'])

# Function to update background if the shared file is changed
def check_background_update():
    new_bg_image = load_background()
    if new_bg_image != bg_label.cget('image'):
        bg_label.config(image=new_bg_image)
        bg_label.image = new_bg_image
    root.after(1000, check_background_update)





#midframe
def quote(quotepic, index):
    random_index = random.randint(0, len(images) - 1)  #Generate a random index
    quotepic.config(image=images_dict[random_index]) 
    root.after(10000, lambda idx=random_index: quote(quotepic, idx))


#botframe

def redirect_rewards(username):
    proc = subprocess.run([sys.executable, "reward_system.py", username])

def redirect_todo():
    proc = subprocess.run([sys.executable, "Mytodo.py", username])

def redirect_music():
    proc = subprocess.run([sys.executable, "Meowmusic.py", username])

def redirect_pomo():
    proc = subprocess.run([sys.executable, "pomodoro.py", username])

def redirect_scratch():
    proc = subprocess.run([sys.executable, "scratchpadv2.py", username])

def redirect_flash():
    proc = subprocess.run([sys.executable, "Meowflashcard.py", username])


#WIDGETS and PACKING-------------------------------------------------

#header
topframe = Frame(root, bg="#FFFFFF", padx=10, pady=5)
topframe.pack(side="top", fill=X)

clocklabel = Label(topframe, font=font_20, bg="#FFFFFF")
clocklabel.grid(row=0, column=2, pady=(5, 0))

daydatelabel = Label(topframe, font=font_15, bg="#FFFFFF")
daydatelabel.grid(row=0, column=1, pady=(5, 0))

rewards_button = Button(topframe, bg="#FFFFFF", borderwidth=0, image=rewards_pic, command=lambda: redirect_rewards(username))
rewards_button.grid(row=0, column=3, rowspan=2, padx=(10, 0), sticky="e")

acc_button = Button(topframe, bg="#FFFFFF", borderwidth=0, image=acc_pic,command=lambda: redirect_acc(username))
acc_button.grid(row=0, column=4, rowspan=2, padx=(10, 0), sticky="e")

info_button = Button(topframe, bg="#FFFFFF", borderwidth=0, image=info_pic, command=redirect_info)
info_button.grid(row=0, column=5, rowspan=2, padx=(10, 0), sticky="e")

topframe.grid_columnconfigure(2, weight=1)


#middle
midframe = Frame(root, bg="#FFFFFF", borderwidth=0)
midframe.pack(expand= TRUE)

quotetitle = Label(midframe, bg="#FFFFFF", image=qtitle)
quotetitle.grid(row=0, column=0, pady=(5))

quotepic = Label(midframe)
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


date_time()
root.mainloop()