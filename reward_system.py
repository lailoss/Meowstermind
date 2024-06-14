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
rewardsbg=PhotoImage(file='./images/reward_bg.png')
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
    c.execute("ALTER TABLE userinfo ADD COLUMN background TEXT ")
    conn.commit()
except sqlite3.OperationalError as e:
    print("OperationalError:", e)
    
#fetch database
c.execute("SELECT background FROM userinfo WHERE username=? ", (username,)) #order by id desc; orders by desc order and LIMIT 1; restricts to just one row (most recent bg chosen)
current_background_result = c.fetchone()
current_background = current_background_result[0] if current_background_result else 'default'
#backgrounds (load image)=================

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

def is_background_unlocked(hours_studied, background_name):
    unlock_requirements = {
        'default': 0,
        'bedroom': 3,
        'cafe': 5,
        'meadow': 10
    }
    required_hours = unlock_requirements.get(background_name, float('inf'))
    return hours_studied >= required_hours

def use_background(bg_name):
    global current_background, total_hours
    if is_background_unlocked(total_hours, bg_name):
        if current_background != bg_name:
            current_background = bg_name
            try:
                c.execute("UPDATE userinfo SET background=? WHERE username=?", (bg_name, username))
                conn.commit()
                
                messagebox.showinfo("Woohoo!", f"Congrats! Your background is set to {bg_name}!")
            except sqlite3.Error as e:
                print(f"Database error: {e}")
                messagebox.showerror("Error", "Failed to update the background in the database.")
        else:
            messagebox.showinfo("Silly Billy!", f"You are already using the {bg_name} background.")
    else:
        required_hours = {
            'default': 0,
            'bedroom': 3,
            'cafe': 5,
            'meadow': 10
        }.get(bg_name, 0)
        hours_you_need=round(required_hours-total_hours,1)
        messagebox.showwarning("Locked", f"Awww, it is locked :( you need {hours_you_need} more hours to unlock it.")


#constants ====================================================
brown = '#A65742'
orange='#F3AB39'
peach='#F8EDD3'


#background buttons-------------------------------------------
#bg a
use_buttona = Button(rewards, text='USE', bg=orange, font='comfortaa 10 bold', bd=0, command=lambda: use_background('default'))
use_buttona.place(x='400', y='245')

#bgb 3 hours
use_buttonb = Button(rewards, text='USE', bg=orange, font='comfortaa 10 bold', bd=0, command=lambda: use_background('bedroom'))
use_buttonb.place(x='640', y='245')

#bg c 5 hours
use_buttonc = Button(rewards, text='USE', bg=orange, font='comfortaa 10 bold', bd=0, command=lambda: use_background('cafe'))
use_buttonc.place(x='640', y='430')

#bg d 10 hours
use_buttond = Button(rewards, text='USE', bg=orange, font='comfortaa 10 bold', bd=0, command=lambda: use_background('meadow'))
use_buttond.place(x='400', y='430')

#hours studied label============================
#display amount of hours studied:
c.execute("SELECT SUM(hours_studied) FROM timer WHERE username=?", (username,))
result = c.fetchone()
total_hours = result[0] if result[0] is not None else 0
total_hours=round(total_hours, 1)

hours_studiedlabel=Label(rewards, text=total_hours, bg=peach, font='comfortaa 18 bold')
hours_studiedlabel.place(x='275', y='23')


rewards.mainloop()
