
from tkinter import *
import pygame
from tkinter import font
from playsound import playsound
import time
from tkinter import messagebox

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
Entry(root, textvariable=hrs, fg='black', width=2, font='arial 40', borderwidth=0, ). place(x='100',y='80')
Label(root, text='HOURS', bg='white').place(x='180',y='120')


mins=StringVar(root, value='00')
Entry(root, textvariable=mins, width='2',fg='black',  font='arial 40',borderwidth=0).place(x='250',y='80')
Label(root,text='MINS', bg='white').place(x='330',y='120')
mins.set("00")

sec=StringVar(root, value='00')
Entry(root, textvariable=sec, width=2,  fg='black', font='arial 40',borderwidth=0, bg='white'). place(x='400',y='80')
Label(root,text='SEC', bg='white').place(x='470',y='120')
sec.set("00")


cycle =1
current_time=None
breaktime=NO



def start_timer():
    global time_run
    global cycle
    time_run=True
    cycle=+1
    timer()
   
def pause_timer():
    global time_run
    time_run=False
    print('timer has paused')
    global current_time
    if current_time is not None:
        root.after_cancel(current_time) #cancels the operation above
   
    global pause_popup
    global pausebg
    pausebg=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\pausepopup.png')
    pause_popup = Toplevel()
    pause_popup.title(f'Don\'t give up!')
    pause_popup.geometry('300x200')
    pause_popup.resizable(False,False)
    pause_popup.iconbitmap(r'./images/sad.ico')
    pause_popupbg=Label(pause_popup,image=pausebg)
    pause_popupbg.pack()
    pausemsg=Label(pause_popup, text='DON’T STOP UNTIL YOU’RE PROUD.', font=('arial 10 bold'), bg='#FAF9F7')
    pausemsg.place(x='35', y='70')
    pause_yes=Label(pause_popup, text='Continue?', font=('calibri 10 bold'), bg='white')
    pause_yes.place(x='120', y='100')      
    yes_button=Button(pause_popup, text='YES, IM A FIGHTER', font=('calibri 10 bold'), bg='#8A9A5B', bd=0)
    yes_button.place(x='30', y='140')
    no_button=Button(pause_popup, text='NO, ILL TRY AGAIN', font=('calibri 10 bold'), bg='white', bd=0)
    no_button.place(x='160', y='140')
    
    

def break_mode():
    print('hellow world')
    global bg_timer
    bg_timer=PhotoImage(file=r'BREAK.png')
    bg.config(image=bg_timer)
    workabutton.destroy()
    workbbutton.destroy()
    workcbutton.destroy()
    break_noti.destroy()
    


def timer():
    global time_run
    global current_time
    total_time = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    
    if total_time > 0:
        
        total_time -= 1
        hrs.set(str(total_time // 3600).zfill(1))
        mins.set(str((total_time % 3600) // 60).zfill(1))
        sec.set(str(total_time % 60).zfill(1))
        current_time= root.after(1000, timer) #starts countdown
        

    
    else:
        global break_noti
        global break_notiimg
        global breaktime
        breaktime=YES

        break_notiimg=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\BREAK_NOTI.png')
        break_noti = Toplevel()
        break_noti.title(f'Break Time!')
        break_noti.geometry('500x300')
        break_noti.resizable(False,False)
        break_noti.iconbitmap(r'./images/break_icon.ico')
        break_notibg=Label(break_noti,image=break_notiimg)
        break_notibg.pack()        
        break_continue=Button(break_noti, text='Proceed', font=('arial 18 bold'), bg='white', bd=0)
        break_continue.place(x='450', y='350')
        break_continuebutton=Button(break_noti, text='PROCEED', font=('calibri 12 bold'), bg='white', bd=1, command=break_mode)
        break_continuebutton.place(x='400', y='250')

global break_continuebutton


  
   
   
def stop_timer():
    global time_run
    time_run=False
    hrs.set('00')
    mins.set('00')
    sec.set('00')







#play, pause and stop buttons
starticon=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\images\start.png')
startbutton=Button(root, text='start', image=starticon,bg='white', borderwidth=0,command=start_timer). place(x='260',y=' 230')
pauseicon=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\images\pause.png')
pausebutton=Button(root, text='pause', image=pauseicon, bg='white', borderwidth=0, command=pause_timer).place(x='200',y='250')
stopicon=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\images\stop.png')
stopbutton=Button(root,text='stop', image=stopicon, bg='white', borderwidth=0, command=stop_timer).place(x='350',y='250')





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

def short_break():
    hrs.set("00")
    mins.set("5")
    sec.set("00")
    
def long_break():
    hrs.set("00")
    mins.set("15")
    sec.set("00")
    


root.mainloop()
root.update()