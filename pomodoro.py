import time
from tkinter import *
import pygame

#consts
red='#d04e2f'

#window
root=Tk()
root.geometry('600x300') 
root.title('Pomodoro Timer')
root.configure(bg='red')
root.iconbitmap(r'./images/pomodoroIcon.ico')



#time tracker
hour=StringVar()
minute=StringVar()
seconds=StringVar()

#load images
workaicon=PhotoImage('./25minicon.png')


def worka():
    minute.set('25')
    seconds.set('00')
    
def workb():
    minute.set('60')
    seconds.set('00')
    
def workc():
    minute.set('120')
    seconds.set('00')
    
def timer():
    totaltime=int(minute.get()*60 + int(seconds.get()))
    
    while totaltime>-1:
        minute,second =(totaltime//60)
    
      
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

minute.set('00')
seconds.set('00')
#custom time - enter in minutes
inputTime=Entry(root, width=5, font=('Arial',20),  textvariable=hour)
inputTime.pack()

#converting entry to integer

#position of time



    



#run time

root.mainloop()
root.update()

