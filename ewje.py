from tkinter import *
import sqlite3
from admin import identry

def create_account_table():
    connect = sqlite3.connect('account.db')
    cursor = connect.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS account (
            username TEXT PRIMARY KEY,
            password TEXT,
            coins INTEGER DEFAULT 0
        )
    ''')
    connect.commit()
    connect.close()

def coins():
    connect = sqlite3.connect('account.db')
    cursor = connect.cursor()
    cursor.execute("PRAGMA table_info(account)")
    columns = [info[1] for info in cursor.fetchall()]
    
    if 'coins' not in columns:
        cursor.execute("ALTER TABLE account ADD COLUMN coins INTEGER DEFAULT 0")
    connect.commit()
    connect.close()

def add_coins(username, coins_added):
    connect = sqlite3.connect('account.db')
    cursor = connect.cursor()
    cursor.execute("UPDATE account SET coins = coins + ? WHERE username = ?", (coins_added, username))
    connect.commit()
    connect.close()

def get_user(username):
    connect = sqlite3.connect('account.db')
    cursor = connect.cursor()
    cursor.execute("SELECT username FROM account WHERE username = ?", (username,))
    user = cursor.fetchone()
    connect.close()
    if user:
        return user[0]
    else:
        raise ValueError("User not found")

if __name__ == "__main__":
    create_account_table()  # Ensure the account table exists
    coins()
    username = identry()  # Assuming this gets the current logged-in username
    get_user(username)  # This checks if the user exists, no need to store in user_id

# window
pom = Tk()
pom.geometry('600x300')
pom.title('Pomodoro Timer')
pom.configure(bg='red')
pom.iconbitmap('./images/pomodoroIcon.ico')
canvas = Canvas()
pom.resizable(False, False)

# consts
red = '#d04e2f'
peach = '#FFE4B6'
bg_img = PhotoImage(file='timer.png')
pink = '#FFC5C5'

# tracker or whatever it's called
cycle = 0
current_time = None
short_breaktime = False
long_breaktime = False
breaktime = False
study_minutes = 0

# background
bg = Label(pom, image=bg_img)
bg.pack()

# time tracker
hrs = StringVar(pom, value='00')
hrs.set("00")
Entry(pom, textvariable=hrs, fg='black', width=2, font='arial 40', borderwidth=0).place(x='100', y='80')
Label(pom, text='HOURS', bg='white').place(x='180', y='120')

mins = StringVar(pom, value='00')
Entry(pom, textvariable=mins, width='2', fg='black', font='arial 40', borderwidth=0).place(x='250', y='80')
Label(pom, text='MINS', bg='white').place(x='330', y='120')
mins.set("00")

sec = StringVar(pom, value='00')
Entry(pom, textvariable=sec, width=2, fg='black', font='arial 40', borderwidth=0, bg='white').place(x='400', y='80')
Label(pom, text='SEC', bg='white').place(x='470', y='120')
sec.set("00")

def start_timer():
    global time_run
    time_run = True
    timer()

def pause_timer():
    global time_run
    time_run = False
    print('timer has paused')
    global current_time
    pom.after_cancel(current_time)  # cancels the operation above

    global pause_popup
    global pausebg
    pausebg = PhotoImage(file='./pausepopup.png')
    pause_popup = Toplevel()
    pause_popup.title("Don't give up!")
    pause_popup.geometry('300x200')
    pause_popup.resizable(False, False)
    pause_popup.iconbitmap('./images/sad.ico')
    pause_popupbg = Label(pause_popup, image=pausebg)
    pause_popupbg.pack()
    pausemsg = Label(pause_popup, text="DON’T STOP UNTIL YOU’RE PROUD.", font=('arial 10 bold'), bg='#FAF9F7')
    pausemsg.place(x='35', y='70')

def stop_timer():
    global time_run
    time_run = False
    hrs.set('00')
    mins.set('00')
    sec.set('00')

def break_mode():
    global bg_timer
    bg_timer = PhotoImage(file='BREAK.png')
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
    global time_run, current_time, breaktime, short_breaktime, long_breaktime, cycle, study_minutes

    total_time = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    cycletext = Label(pom, text='ROUND ' + str(cycle), font='comfortaa 12 bold', background='#FF4545')
    cycletext.place(x='80', y='33')

    if total_time > 0:
        total_time -= 1
        hrs.set(str(total_time // 3600).zfill(2))
        mins.set(str((total_time % 3600) // 60).zfill(2))
        sec.set(str(total_time % 60).zfill(2))
        current_time = pom.after(1000, timer)  # starts countdown

    else:  # timer 00
        if not breaktime:
            global break_noti, break_notiimg
            breaktime = True
            cycle += 1
            is_breaktime()
            study_minutes += 20
            if study_minutes >= 20:
                add_coins(username, 5)
                study_minutes = 0
            break_presets()
            break_notiimg = PhotoImage(file='BREAK_NOTI.png')
            break_noti = Toplevel()
            break_noti.title('Break Time!')
            break_noti.geometry('500x300')
            break_noti.resizable(False, False)
            break_noti.iconbitmap('./images/break_icon.ico')
            break_notibg = Label(break_noti, image=break_notiimg)
            break_notibg.pack()
            break_mode()
        else:
            global study_noti, studynotiimg
            breaktime = False
            study_mode()

            studynotiimg = PhotoImage(file='STUDY_NOTI.png')
            study_noti = Toplevel()
            study_noti.title('Study Time!')
            study_noti.geometry('500x300')
            study_noti.resizable(False, False)
            study_noti.iconbitmap(r'./images/break_icon.ico')
            study_notibg = Label(study_noti, image=studynotiimg)
            study_notibg.pack()
            studynotigone()

def is_breaktime():
    global short_breaktime, long_breaktime
    if cycle % 4 == 0:
        short_breaktime = False
        long_breaktime = True
    else:
        long_breaktime = False
        short_breaktime = True

def break_presets():
    work_duration = int(hrs.get()) * 60 + int(mins.get())

    if work_duration <= 25:
        if short_breaktime:
            hrs.set("00")
            mins.set("05")
            sec.set("00")
        elif long_breaktime:
            hrs.set("00")
            mins.set("15")
            sec.set("00")
    elif work_duration <= 40:
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

# time presets
def worka():
    hrs.set("00")
    mins.set("05")
    sec.set("00")

def workb():
    hrs.set('00')
    mins.set('40')
    sec.set('00')

def workc():
    hrs.set('01')
    mins.set('00')
    sec.set('00')

#
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
