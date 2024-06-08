from tkinter import *
import sys
import sqlite3
import os
from tkinter import messagebox
#window
rewards=Tk()
rewards.geometry('800x500')
rewards.title ('Wallpapers by Itang!')
rewards.resizable(False, False)
rewardsbg=PhotoImage(file='reward_bg.png')
bg=Label(rewards,image=rewardsbg)
bg.pack()

#background in database = current background tq
#gets username from login
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("username not provided :()")
    sys.exit(1)
    
conn = sqlite3.connect('database.db')
c = conn.cursor()

#create database

try:
    c.execute("ALTER TABLE timer ADD COLUMN background TEXT, unlocked_bg TEXT ")
    conn.commit()
except sqlite3.OperationalError as e:
    print("OperationalError:", e)
    

# Function to check if a background is unlocked 
def is_background_unlocked(username, background):
    c.execute("SELECT 1 FROM unlocked_backgrounds WHERE username=? AND background=? LIMIT 1", (username, background))
    return c.fetchone() is not None

# Function to unlock a background
def unlock_background(username, background):
    if not is_background_unlocked(username, background):
        c.execute("INSERT INTO unlocked_backgrounds (username, background) VALUES (?, ?)", (username, background))
        conn.commit()

    
#fetch database
c.execute("SELECT background FROM timer WHERE username=? ORDER BY id DESC LIMIT 1", (username,)) #order by id desc; orders by desc order and LIMIT 1; restricts to just one row (most recent bg chosen)
current_background_result = c.fetchone()
current_background = current_background_result[0] if current_background_result else 'default'
#backgrounds=================

bgdefault=PhotoImage(file='./backgrounds/default.png')
bgcafe=PhotoImage(file='./backgrounds/cafe.png')
bgmeadow=PhotoImage(file='./backgrounds/meadow.png')
bgbedroom=PhotoImage(file='./backgrounds/bedroom.png')

#backgrounds--------------------
backgrounds = {
    'default': bgdefault,
    'bedroom': bgbedroom,
    'cafe': bgcafe,
    'meadow': bgmeadow
    
}
bg_image = backgrounds.get(current_background, backgrounds['default'])

#stay LOCKED 
def has_unlocked_background(username, background_name):
    c.execute("SELECT unlocked_bg FROM timer WHERE username=?", (username,))
    result = c.fetchone()
    if result and result[0]:
        unlocked_backgrounds = result[0].split(',')
        return background_name in unlocked_backgrounds
    return False

def use_background(bg_name, hours_required):
    global current_background, total_hours
    if has_unlocked_background(username, bg_name):
        if current_background != bg_name:
            current_background = bg_name
            c.execute("UPDATE timer SET background=? WHERE username=?", (bg_name, username))
            conn.commit()
            messagebox.showinfo("Woohoo!", f"Congrats! Your background set to {bg_name}!")
        else:
            messagebox.showinfo("Silly Billy!", f"You are already using the {bg_name} background.")
    else:
        if total_hours >= hours_required:
            current_background = bg_name
            c.execute("UPDATE timer SET background=?, unlocked_bg = COALESCE(unlocked_bg || ',', '') || ? WHERE username=?", (bg_name, bg_name, username))
            conn.commit()
            messagebox.showinfo("Woohoo!", f"Congrats! Your background set to {bg_name}!")
        else:
            messagebox.showwarning("Locked", f"This background is locked. You need {hours_required - total_hours} more hours to unlock it.")




#constants ====================================================
brown = '#A65742'
orange='#F3AB39'
peach='#F8EDD3'


#background buttons-------------------------------------------
#bg a
use_buttona = Button(rewards, text='USE', bg=orange, font='comfortaa 10 bold', bd=0, command=lambda: use_background('default', 0))
use_buttona.place(x='400', y='245')

#bgb 3 hours
use_buttonb = Button(rewards, text='USE', bg=orange, font='comfortaa 10 bold', bd=0, command=lambda: use_background('bedroom', 3))
use_buttonb.place(x='640', y='245')

#bg c 5 hours
use_buttonc = Button(rewards, text='USE', bg=orange, font='comfortaa 10 bold', bd=0, command=lambda: use_background('cafe', 5))
use_buttonc.place(x='640', y='430')

#bg d 10 hours
use_buttond = Button(rewards, text='USE', bg=orange, font='comfortaa 10 bold', bd=0, command=lambda: use_background('meadow', 100))
use_buttond.place(x='400', y='430')

#hours studied label============================
#display amount of hours studied:
c.execute("SELECT SUM(hours_studied) FROM timer WHERE username=?", (username,))
result = c.fetchone()
total_hours = result[0] if result[0] is not None else 0

hours_studiedlabel=Label(rewards, text=total_hours, bg=peach, font='comfortaa 18 bold')
hours_studiedlabel.place(x='275', y='23')


rewards.mainloop()
