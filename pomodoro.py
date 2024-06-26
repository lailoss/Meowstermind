import random
from tkinter import *
import pygame
from tkinter import font
import time
import os
from tkinter import messagebox
import sqlite3
import sys

pygame.mixer.init()

#gets username from login
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("username not provided :()")
    sys.exit(1)
    
    
#create table
conn = sqlite3.connect('database.db')
c = conn.cursor()

# create table
c.execute('''
    CREATE TABLE IF NOT EXISTS timer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hours_studied REAL,
        username TEXT
    )
''')
conn.commit()

#window
pom=Tk()
pom.geometry('600x300') 
pom.title('Pomodoro Timer')
pom.configure(bg='red')

canvas = Canvas()
pom.resizable(False, False)

   
#consts
red='#FFFAF2' #please note that this is not actually red, im just lazy to change everything tq
peach='#FFE4B6'
bg_img=PhotoImage(file='./images/timer.png')
pink='#FFC5C5'

#tracker or whatever it's called
cycle =0
current_time=None
short_breaktime=False
long_breaktime=False
breaktime=False
total_hours=0
paused_position=None
time_run=False

#background-------------------------------------------
bg=Label(pom, image=bg_img)
bg.pack()

#time tracker---------------------------------------------------
hrs = StringVar(pom)
hrs.set("00")
Entry(pom, textvariable=hrs, fg='black', width=2, font='arial 40', borderwidth=0, ). place(x='100',y='80')
Label(pom, text='HOURS', bg='white').place(x='180',y='120')

mins=StringVar(pom)
Entry(pom, textvariable=mins, width='2',fg='black',  font='arial 40',borderwidth=0).place(x='250',y='80')
Label(pom,text='MINS', bg='white').place(x='330',y='120')
mins.set("00")

sec=StringVar(pom)
Entry(pom, textvariable=sec, width=2,  fg='black', font='arial 40',borderwidth=0, bg='white'). place(x='400',y='80')
Label(pom,text='SEC', bg='white').place(x='470',y='120')
sec.set("00")

print('Initial value of hrs:', hrs.get())
print('Initial value of mins:', mins.get())
print('Initial value of sec:', sec.get())



# play selected song---------------------------------------------------
# Initialize pygame mixer and set the end event for music
pygame.mixer.music.set_endevent(pygame.USEREVENT)

playlist = []
current_song_index = 0  # Index to track current song in playlist
paused_position = None  # Position to resume music after pause

# Function to load selected songs from the database
def load_selected_songs():
    try:
        c.execute("SELECT song_path FROM playlist WHERE username = ?", (username,))
        songs = c.fetchall()
        return [song[0] for song in songs]
    except Exception as e:
        print(f"Error loading playlist: {e}")
        return []

# Load the playlist when the script starts
playlist = load_selected_songs()

# Function to play a random song from the playlist
def play_random_song():
    global paused_position
    if playlist:
        random_song = random.choice(playlist)
        pygame.mixer.music.load(random_song)
        pygame.mixer.music.play()
        
# Event handler for song end
def song_end(event):
    if event.type == pygame.USEREVENT:
        play_random_song()


#warning; lots of FUNCTIONS----------------------------------------
# Start the timer and play the selected song
def start_timer():
    global paused_position, initial_study_time, start_time, time_run
    
    if not time_run:  # Only start the timer if it's not already running
        initial_study_time = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
        start_time = time.time()

        if paused_position is not None:
            # Resume from the paused position if music was paused
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_pos(paused_position)
            paused_position = None  # Clear the paused position
        elif not pygame.mixer.music.get_busy() and playlist:
            # No music is playing, start playing a new song if there is a playlist
            play_random_song()

        time_run = True
        timer()

      
def pause_timer():
    global time_run, paused_position, current_song_index
    time_run = False
    if pygame.mixer.music.get_busy():
        paused_position = pygame.mixer.music.get_pos() / 1000.0
        pygame.mixer.music.pause()  # Pause the music
    else:
        paused_position = None  # No music playing, set paused_position to None
    current_song_index -= 1
    pom.after_cancel(current_time)  # cancels the operation above
   
    global pause_popup
    global pausebg
    pausebg=PhotoImage(file='./images/pausepopup.png')
    pause_popup = Toplevel()
    pause_popup.title(f'Don\'t give up!')
    pause_popup.geometry('300x200')
    pause_popup.resizable(False,False)
    pause_popup.iconbitmap('./images/sad.ico')
    pause_popupbg=Label(pause_popup,image=pausebg)
    pause_popupbg.pack()
    pausemsg=Label(pause_popup, text='DON’T STOP UNTIL YOU’RE PROUD.', font=('arial 10 bold'), bg='#FAF9F7')
    pausemsg.place(x='35', y='70')


def stop_timer():
    global time_run
    time_run=False
    hrs.set('00')
    mins.set('00')
    sec.set('00')

def break_mode():
    print('break mode started')
    global bg_timer
    bg_timer=PhotoImage(file='./images/BREAK.png')
    bg.config(image=bg_timer)
     
    
def study_mode():
    bg.config(image=bg_img)
    hrs.set('00')
    mins.set('00')
    sec.set('00')
    print('study mode')
   
    
    
    
initial_study_time = 0

def start_break_timer():
    global initial_break_time, time_run
    initial_break_time = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    time_run = True
    timer()  

def timer():
    global time_run, current_time, breaktime,short_breaktime, long_breaktime, cycle, study_mode, total_hours, initial_study_time
   
    total_time = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    cycletext=Label(pom, text='ROUND '+ str(cycle), font='comfortaa 12 bold', background=red)
    cycletext.place(x='80', y='33')
    
    if total_time > 0 :
        total_time -= 1
        hrs.set(str(total_time // 3600).zfill(2))
        mins.set(str((total_time % 3600) // 60).zfill(2))
        sec.set(str(total_time % 60).zfill(2))
        current_time= pom.after(1000, timer) #starts countdown  
        
    else: #timer 00

        if not breaktime:
            breaktime=True
            cycle+=1
            is_breaktime()
            break_presets()
            break_mode()
            start_break_timer()
            
            studied_seconds = initial_study_time
            print("Total time spent studying (in seconds):", studied_seconds)

            hours_studied = studied_seconds / 3600.0
            c.execute("INSERT INTO timer (hours_studied, username) VALUES (?, ?)", (hours_studied, username))
            conn.commit()
            print("Study time inserted into database successfully.")
            
        else:
            breaktime = False
            study_mode()
            time_run = False
        

def is_breaktime():
    global short_breaktime, long_breaktime
    if cycle%4==0:
        short_breaktime=False
        long_breaktime=True
    else:
        long_breaktime=False
        short_breaktime = True
                
    
def break_presets():
    work_duration= int(hrs.get())*60 +int(mins.get())
   
    if work_duration <=25:
            if short_breaktime:
                hrs.set("00")
                mins.set("00")
                sec.set("03")
            elif long_breaktime:
                hrs.set("00")
                mins.set("15")
                sec.set("00")
    elif work_duration <=40:
            if short_breaktime:
                hrs.set("00")
                mins.set("10")
                sec.set("00")
            elif long_breaktime:
                hrs.set("00")
                mins.set("20")
                sec.set("00")
    else:
            if short_breaktime:
                hrs.set("00")
                mins.set("15")
                sec.set("00")
            elif long_breaktime:
                hrs.set("00")
                mins.set("25")
                sec.set("00")

#time presets-and boring stuff----------------------------------------
def worka():
    hrs.set("00")
    mins.set("00")
    sec.set("5")
    if breaktime:
        break_presets()

    
def workb():
    hrs.set('00')
    mins.set('40')
    sec.set('00')
    if breaktime:
        break_presets()

def workc():
    hrs.set('01')
    mins.set('00')
    sec.set('00')
    if breaktime:
        break_presets()


#play, pause and stop buttons
starticon=PhotoImage(file='./images/start.png')
startbutton=Button(pom, text='start', image=starticon,bg='white', borderwidth=0,command=start_timer). place(x='285',y=' 240')
pauseicon=PhotoImage(file='./images/pause.png')
pausebutton=Button(pom, text='pause', image=pauseicon, bg='white', borderwidth=0, command=pause_timer).place(x='200',y='250')
stopicon=PhotoImage(file='./images/stop.png')
stopbutton=Button(pom,text='stop', image=stopicon, bg='white', borderwidth=0, command=stop_timer).place(x='350',y='250')

    
moyen=PhotoImage(file='./images/MOYEN.png')
moolan=PhotoImage(file='./images/MOOLAN.png')
maria=PhotoImage(file='./images/MARIA.png')
workabutton=Button(pom, image=moyen, bg=pink, font='comfortaa 18 bold', borderwidth=0, command=worka)
workabutton.place(x='175',y=' 160')
workbbutton=Button(pom, image=moolan, bg=pink, font='comfortaa 18 bold', borderwidth=0, command=workb)
workbbutton.place(x='270',y=' 160')
workcbutton=Button(pom, image=maria, bg=pink, font='comfortaa 18 bold', borderwidth=0, command=workc)
workcbutton.place(x='365',y=' 160')

# Load the playlist and handle song end events
playlist = load_selected_songs()
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.mixer.music.set_volume(0.5)  # Adjust volume if needed

pom.mainloop()


