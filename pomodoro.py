import time
from tkinter import *
import pygame

pygame.init()
#consts
red='#d04e2f'
peach='#FFE4B6'
beep=pygame. mixer.music.load('pomodoro_beep.mp3')

#window
root=Tk()
root.geometry('600x300') 
root.title('Pomodoro Timer')
root.configure(bg='red')
root.iconbitmap(r'./images/pomodoroIcon.ico')



#time tracker

mins=StringVar()
Entry(root, textvariable='mins', height='10', width='5',fg=peach).place(x='250',y='100')
Label(root,text='minutes').place(x='250',y='200')

sec=StringVar()
Entry(root, textvariable='sec', fg=peach). place(x='200',y='200')
Label(root,text='seconds').place(x='300',y='200')

hrs = StringVar()
Entry(root, textvariable='hours', fg=peach). place(x='200',y='200')
Label(root, text='hours').place(x='250',y='200')

hrs.set('00')
mins.set('00')
sec.set('00')


#load images
workaicon=PhotoImage('./25minicon.png')


startbutton=Button(root, text='start'). place(x='300',y=' 270')
pausebutton=Button(root, text='pause').place(x='250',y='270')
stopbutton=Button(root,text='stop').place(x='350',y='270')

def worka():
    hrs.set('00')
    mins.set('250')
    sec.set('00')
    
def workb():
    hrs.set('00')
    mins.set('60')
    sec.set('00')
    
def workc():
    hrs.set('2')
    mins.set('00')
    sec.set('00')
    
def timer():
    totaltime=int(hrs.get()*3600 +int(mins.get())*60 + int(sec.get()))
    
    while totaltime>-1:
        minute,second =(totaltime//60,totaltime%60)
    hours == 0
    if minute> 60:
        hours, minute=(minute//60, minute%60)
    sec.set(second)
    mins.set(minute)
    hrs.set(hours)
    
    root.update()
    time.sleep(1) #halts execution for x sec
    
    if totaltime==0:
        pygame.mixer.play(beep)
        
    
    
#time presets
worka=25 * 60
workb=60 * 60
workc=120 * 60
breaka=5*60
breakb=10*60
breakc=20*60
worka_button=Button(root, image=workaicon, command=worka)
workb_button=Button(root, text='60 min', bg='red', fg='#fffdfd', command=workb)
workc_button=Button(root, text='120 min', bg='red', fg='#fffdfd', command=workc)
worka_button.place(x=50, y=40)
workb_button.place(x=70, y=40)
workc_button.place(x=100, y=40)


#custom time - enter in minutes


#converting entry to integer

#position of time



    



#run time

root.mainloop()
root.update()

