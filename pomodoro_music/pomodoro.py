import random
from tkinter import *
import pygame
from tkinter import font
import time
import os
from tkinter import messagebox

pygame.mixer.init()

#window
pom=Tk()
pom.geometry('600x300') 
pom.title('Pomodoro Timer')
pom.configure(bg='red')
pom.iconbitmap('./images/pomodoroIcon.ico')
canvas = Canvas()
pom.resizable(False, False)

#consts
red='#d04e2f'
peach='#FFE4B6'
#beep=pygame. mixer.music.load('pomodoro_beep.mp3')
bg_img=PhotoImage(file='timer.png')
pink='#FFC5C5'

#tracker or whatever it's called
cycle =0
current_time=None
short_breaktime=False
long_breaktime=False
breaktime=False
time_run = 0
paused_position = None

#background
bg=Label(pom, image=bg_img)
bg.pack()

#time tracker
hrs = StringVar(pom, value='00')
hrs.set("00")
Entry(pom, textvariable=hrs, fg='black', width=2, font='arial 40', borderwidth=0, ). place(x='100',y='80')
Label(pom, text='HOURS', bg='white').place(x='180',y='120')

mins=StringVar(pom, value='00')
Entry(pom, textvariable=mins, width='2',fg='black',  font='arial 40',borderwidth=0).place(x='250',y='80')
Label(pom,text='MINS', bg='white').place(x='330',y='120')
mins.set("00")

sec=StringVar(pom, value='00')
Entry(pom, textvariable=sec, width=2,  fg='black', font='arial 40',borderwidth=0, bg='white'). place(x='400',y='80')
Label(pom,text='SEC', bg='white').place(x='470',y='120')
sec.set("00")


# Play selected song
def play_selected_song():
    with open("selected_songs.txt", "r") as file:
        songs = file.readlines()
    if songs:
        song = random.choice(songs).strip()
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
    #try:
        #with open("selected_song.txt", "r") as file:
            #songs = [line.strip() for line in file.readlines()]

        #for song_path in songs:
            #pygame.mixer.music.load(song_path)
            #pygame.mixer.music.play()
        #2 try:
        #with open("selected_song.txt", "r") as file:
        #    song_path = file.read()
        #pygame.mixer.music.load(song_path)
        #pygame.mixer.music.play(loops=0)
            
    #except Exception as e:
        #messagebox.showerror("Error", f"Could not play song: {e}")

def start_timer():
    global paused_position
    global time_run

    if paused_position is not None:
        # Resume from the paused position
        pygame.mixer.music.unpause()
        pygame.mixer.music.set_pos(paused_position)
    else:
        # Play the song when the timer starts
        play_selected_song()
    
    time_run = True
    timer()
    
   
def pause_timer():
    global time_run, paused_position
    time_run=False
    paused_position = pygame.mixer.music.get_pos() / 1000.0
    pygame.mixer.music.pause()  # Pause the music
    print('timer has paused')
    global current_time
    pom.after_cancel(current_time) #cancels the operation above
   
    global pause_popup
    global pausebg
    pausebg=PhotoImage(file='./pausepopup.png')
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
    print('hellow world')
    global bg_timer
    bg_timer=PhotoImage(file='BREAK.png')
    bg.config(image=bg_timer)
    break_noti.destroy()
    
    
def study_mode():
    bg.config(image=bg_img)
    hrs.set('00')
    mins.set('00')
    sec.set('00')
    
def studynotigone():
    study_noti.destroy()

    
def timer():
    global time_run, current_time, breaktime,short_breaktime, long_breaktime, cycle, study_mode
   
    total_time = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    cycletext=Label(pom, text='ROUND '+ str(cycle), font='comfortaa 12 bold', background='#FF4545')
    cycletext.place(x='80', y='33')
    
    if total_time > 0:
        total_time -= 1
        hrs.set(str(total_time // 3600).zfill(1))
        mins.set(str((total_time % 3600) // 60).zfill(1))
        sec.set(str(total_time % 60).zfill(1))
        current_time= pom.after(1000, timer) #starts countdown  
        
    else: #timer 00
        if not breaktime:
            global break_noti,  break_notiimg
            breaktime=True
            cycle+=1
            is_breaktime()
            break_presets()
            break_notiimg=PhotoImage(file='BREAK_NOTI.png')
            break_noti = Toplevel()
            break_noti.title(f'Break Time!')
            break_noti.geometry('500x300')
            break_noti.resizable(False,False)
            break_noti.iconbitmap('./images/break_icon.ico')
            break_notibg=Label(break_noti,image=break_notiimg)
            break_notibg.pack()        
            break_mode()
        else:
            global study_noti, studynotiimg 
            breaktime=False
            study_mode()
                
            studynotiimg=PhotoImage(file='STUDY_NOTI.png')
            study_noti = Toplevel()
            study_noti.title(f'Study Time!')
            study_noti.geometry('500x300')
            study_noti.resizable(False,False)
            study_noti.iconbitmap(r'./images/break_icon.ico')
            study_notibg=Label(study_noti,image=studynotiimg)
            study_notibg.pack()
            studynotigone()





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

#time presets
def worka():
    hrs.set("00")
    mins.set("00")
    sec.set("5")

    
def workb():
    hrs.set('00')
    mins.set('40')
    sec.set('00')

def workc():
    hrs.set('01')
    mins.set('00')
    sec.set('00')

#play, pause and stop buttons
starticon=PhotoImage(file='./images/start.png')
startbutton=Button(pom, text='start', image=starticon,bg='white', borderwidth=0,command=start_timer). place(x='260',y=' 230')
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


pom.mainloop()
pom.update()
