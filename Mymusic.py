from tkinter import*
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root=Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#1E2647")
root.resizable(False,False)

mixer.init()

def open_folder():
    path= filedialog.askdirectory()
    if path:
        os.chdir(path)
        Songs=os.listdir(path)
##        print(Songs)
        for song in Songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)
                
def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

# top
Top=PhotoImage(file="top.png")
Label(root,image=Top).pack()

# button
play_button=PhotoImage(file="play.png")
Button(root,image=play_button,bg="#1E2647",bd=0,command=play_song).place(x=100,y=400)

stop_button=PhotoImage(file="stop.png")
Button(root,image=stop_button,bg="#1E2647",bd=0,command=mixer.music.stop).place(x=30,y=500)

pause_button=PhotoImage(file="pause.png")
Button(root,image=pause_button,bg="#1E2647",bd=0,command=mixer.music.pause).place(x=115,y=500)

resume_button=PhotoImage(file="resume.png")
Button(root,image=resume_button,bg="#1E2647",bd=0,command=mixer.music.unpause).place(x=200,y=500)

# label
music=Label(root,text="",font=("arial",10,"bold"),fg="black")
music.place(x=150,y=340,anchor="center")

# music
Menu=PhotoImage(file="menu.png")
Label(root,image=Menu).pack(padx=10,pady=50,side=RIGHT)

music_frame = Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=330,y=350,width=560,height=250)

Button(root,text="Open Folder",width=15,height=2,font=("Arial",10,"bold"),fg="white",bg="#233A4D",command=open_folder).place(x=330,y=300)

scroll = Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial",10),bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT,fill=BOTH)

root.mainloop()