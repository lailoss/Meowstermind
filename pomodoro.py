
from tkinter import *
import pygame
from tkinter import font
import time

pygame.init()



#window
root=Tk()
root.geometry('600x300') 
root.title('Pomodoro Timer')
root.configure(bg='red')
root.iconbitmap(r'./images/pomodoroIcon.ico')
canvas = Canvas()
root.resizable(False, False)

#consts
red='#d04e2f'
peach='#FFE4B6'
beep=pygame. mixer.music.load('pomodoro_beep.mp3')
bg_img=PhotoImage(file=r'./timer.png')
pink='#FFC5C5'


    

bg=Label(root, image=bg_img)
bg.pack()
#time tracker

hrs = StringVar(root, value='00')
hrs.set("00")
Entry(root, textvariable=hrs, fg='black', width=2, font='arial 40', borderwidth=2, ). place(x='100',y='80')
Label(root, text='HOURS', bg='white').place(x='180',y='120')


mins=StringVar(root, value='00')
Entry(root, textvariable=mins, width='2',fg='black',  font='arial 40',borderwidth=2).place(x='250',y='80')
Label(root,text='MINS', bg='white').place(x='330',y='120')
mins.set("00")

sec=StringVar(root, value='00')
Entry(root, textvariable=sec, width=2,  fg='black', font='arial 40',borderwidth=2, bg='white'). place(x='400',y='80')
Label(root,text='SEC', bg='white').place(x='470',y='120')
sec.set("00")

def timer():
    total_time = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    
    if total_time > 0:
        total_time -= 1
        hrs.set(str(total_time // 3600).zfill(2))
        mins.set(str((total_time % 3600) // 60).zfill(2))
        sec.set(str(total_time % 60).zfill(2))
        root.after(1000, timer)
    else:
        pygame.mixer.Sound.play(beep)

#play, pause and stop buttons
def start_timer():
    timer()
    
def pause_timer():
    hrs.set()


#play, pause and stop buttons
starticon=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\images\start.png')
startbutton=Button(root, text='start', image=starticon,bg='white', borderwidth=0,command=start_timer). place(x='260',y=' 230')
pauseicon=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\images\pause.png')
pausebutton=Button(root, text='pause', image=pauseicon, bg='white', borderwidth=0).place(x='200',y='250')
stopicon=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\images\stop.png')
stopbutton=Button(root,text='stop', image=stopicon, bg='white', borderwidth=0).place(x='350',y='250')


#time presets
def worka():
    hrs.set("00")
    mins.set("25")
    sec.set("00")
    
def workb():
    hrs.set('01')
    mins.set('00')
    sec.set('00')
    
def workc():
    hrs.set('2')
    mins.set('00')
    sec.set('00')
    
workabutton=Button(root, text='25 MIN', bg=pink, font='comfortaa 18 bold', borderwidth=0, command=worka)
workabutton.place(x='80',y=' 160')
workbbutton=Button(root, text='60 MIN', bg=pink, font='comfortaa 18 bold', borderwidth=0, command=workb)
workbbutton.place(x='250',y=' 160')
workcbutton=Button(root, text='120 MIN', bg=pink, font='comfortaa 18 bold', borderwidth=0, command=workc)
workcbutton.place(x='410',y=' 160')

 

root.mainloop()
root.update()

