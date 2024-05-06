from tkinter import *
import pygame
from tkinter import font
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

#tracker or whatever it's called
cycle =1
current_time=None
short_breaktime=False
long_breaktime=False
breaktime=False


#backgground
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

#starts time
def start_timer():
    global time_run
    time_run=True
    timer()
   
def pause_timer():
    global time_run
    time_run=False
    print('timer has paused')
    global current_time
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
    

   
def stop_timer():
    global time_run
    time_run=False
    hrs.set('00')
    mins.set('00')
    sec.set('00')
    

def break_mode():
    print('hellow world')
    global bg_timer
    bg_timer=PhotoImage(file=r'BREAK.png')
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
    cycletext=Label(root, text='ROUND '+ str(cycle), font='comfortaa 12 bold', background='#FF4545')
    cycletext.place(x='80', y='33')
    
    if total_time > 0:
        total_time -= 1
        hrs.set(str(total_time // 3600).zfill(1))
        mins.set(str((total_time % 3600) // 60).zfill(1))
        sec.set(str(total_time % 60).zfill(1))
        current_time= root.after(1000, timer) #starts countdown  
        
           
    
    
    else: #timer 00
        if not breaktime:
            global break_noti,  break_notiimg
            breaktime=True
            cycle+=1
            is_breaktime()
            break_presets()
            break_notiimg=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\BREAK_NOTI.png')
            break_noti = Toplevel()
            break_noti.title(f'Break Time!')
            break_noti.geometry('500x300')
            break_noti.resizable(False,False)
            break_noti.iconbitmap(r'./images/break_icon.ico')
            break_notibg=Label(break_noti,image=break_notiimg)
            break_notibg.pack()        
            break_continuebutton=Button(break_noti, text='PROCEED', font=('calibri 12 bold'), bg='white', bd=1, command=break_mode)
            break_continuebutton.place(x='400', y='250')
        else:
            global study_noti, studynotiimg 
            breaktime=False
            study_mode()
                
            studynotiimg=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\STUDY_NOTI.png')
            study_noti = Toplevel()
            study_noti.title(f'Study Time!')
            study_noti.geometry('500x300')
            study_noti.resizable(False,False)
            study_noti.iconbitmap(r'./images/break_icon.ico')
            study_notibg=Label(study_noti,image=studynotiimg)
            study_notibg.pack()
            studycontinuebutton=Button(study_noti, text='PROCEED', font=('calibri 12 bold'), bg='white', bd=1, command=studynotigone)
            studycontinuebutton.place(x='400', y='250')
            
            




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
starticon=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\images\start.png')
startbutton=Button(root, text='start', image=starticon,bg='white', borderwidth=0,command=start_timer). place(x='260',y=' 230')
pauseicon=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\images\pause.png')
pausebutton=Button(root, text='pause', image=pauseicon, bg='white', borderwidth=0, command=pause_timer).place(x='200',y='250')
stopicon=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\images\stop.png')
stopbutton=Button(root,text='stop', image=stopicon, bg='white', borderwidth=0, command=stop_timer).place(x='350',y='250')


    
moyen=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\images\MOYEN.png')
moolan=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\images\MOOLAN.png')
maria=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\images\MARIA.png')
workabutton=Button(root, image=moyen, bg=pink, font='comfortaa 18 bold', borderwidth=0, command=worka)
workabutton.place(x='175',y=' 160')
workbbutton=Button(root, image=moolan, bg=pink, font='comfortaa 18 bold', borderwidth=0, command=workb)
workbbutton.place(x='270',y=' 160')
workcbutton=Button(root, image=maria, bg=pink, font='comfortaa 18 bold', borderwidth=0, command=workc)
workcbutton.place(x='365',y=' 160')




root.mainloop()
root.update()