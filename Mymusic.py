from tkinter import*
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os
import customtkinter
import pygame

root = customtkinter.CTk()
root.title("Meow Music")
root.geometry("1200x700")
root.resizable(False,False)

# Initialise Pygame Mixer
pygame.mixer.init()

def open_folder():
    path= filedialog.askdirectory()
    if path:
        os.chdir(path)
        Songs=os.listdir(path)
##        print(Songs)
        for song in Songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)
   
# Play Button             
def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])
    
# Create global pause
global paused
paused = False 
# Pause and Unpause the current song
def pause(is_paused):
    global paused
    paused = is_paused
    
    if paused:
        #unpause
        pygame.mixer.music.unpause()
        paused = False
        
    else:
         #Pause
        pygame.mixer.music.pause()
        paused = True

# Stop playing current song
global stopped
stopped = False
def stop():
    
    # Stop song from playing
    pygame.mixer.music.stop()
    playlist.selection_clear(ACTIVE)
    
    # Set stop variable to true
    global stopped
    stopped = True
    
def previous_song():
   # Get the current song tuple number
    next_one = playlist.curselection()
    print("Current song index:", next_one)
    # Subtract one from the current song number
    next_one = next_one[0] - 1
    print("Previous song index:", next_one)
    
    if next_one < 0:
        next_one = 0  # Ensure it doesn't go below 0
    
    # Grab song title from playlist
    song = playlist.get(next_one)
    # Add directory structure and mp3 to song title
    song_path = f'C:/Users/Fawqan/Meowstermind/Songs/{song}'
    print("Previous song:", song_path)
    
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
    # Update label with current song title
    music.config(text=song[0:-4])
    
    # Clear active bar in playlist listbox
    playlist.selection_clear(0, END)
    
    # Activate the new song bar
    playlist.activate(next_one)
    
    # Set Active bar to next song
    playlist.selection_set(next_one, last=None)
    
    # Activate new song bar
    playlist.activate(next_one)
    
 
def next_song():
    # Get the current song tuple number
    current_index = playlist.curselection()[0]
    
    # Add one to the current song number
    next_index = current_index + 1
    
     # Check if the next song index exceeds the total number of songs
    if next_index >= playlist.size():
        next_index = 0  # Loop back to the beginning
        
    # Grab the title of the next song from the playlist
    next_song_title = playlist.get(next_index)
    
    # Construct the file path for the next song
    next_song_path = f'C:/Users/Fawqan/Meowstermind/Songs/{next_song_title}'
    
    # Load and play song
    pygame.mixer.music.load(next_song_path)
    pygame.mixer.music.play(loops=0)
    
    # Update label with current song title
    music.config(text=next_song_title[0:-4])
    
    # Clear active bar in playlist listbox
    playlist.selection_clear(0, END)
    
    # Activate the new song in the playlist
    playlist.activate(next_index)
    
    # Set the selection to the new song
    playlist.selection_set(next_index)
    
# Create slider function
def slide(x):
    #slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
    song = playlist.get(ACTIVE)
    song = f'C:/Users/Fawqan/Meowstermind/Songs/{song}'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))
    
    ##### still have the problem with the slider ######

# Create Volume Function
def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())
    
# outer frame
outer_frame_width = 800
outer_frame_height = 500
outer_frame = customtkinter.CTkFrame(root, width=outer_frame_width, height=outer_frame_height,corner_radius= 10 ,fg_color="#1E2647")
outer_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# inner frame
inner_frame_width = 700
inner_frame_height = 350
inner_frame = customtkinter.CTkFrame(outer_frame, width=inner_frame_width, height=inner_frame_height, corner_radius=5, fg_color="#EFE0BF")
inner_frame.place(relx=0.5, rely=0.6, anchor=CENTER)

# cat wearing headphone image
image1 = PhotoImage(file="headphonecat.png").subsample(10)
headphone_cat = Label(outer_frame, image=image1, bg='#1E2647')  # Set the background color to match the outer frame
headphone_cat.place(x=10, y=13)

# music logo image
image2 = PhotoImage(file="musiclogo.png").subsample(13)
music_logo = Label(outer_frame, image=image2, bg='#1E2647')  # Set the background color to match the outer frame
music_logo.place(x=430, y=30)


# font and title
font1 = ('Arial',50,'bold')
font2 = ('Arial',10,'bold')
font3 = ('Arial',10,'bold')

title_label = customtkinter.CTkLabel(root,font=font1,text='Meow Music',text_color='#EFE0BF',bg_color='#1E2647')
title_label.place(x=370,y=160)

# button
# Define Player Control Button Images
back_btn_img = PhotoImage(file="back.png")
foward_btn_img = PhotoImage(file="foward.png")
play_btn_img = PhotoImage(file="play.png")
pause_btn_img = PhotoImage(file="pause.png")
stop_btn_img = PhotoImage(file="stop.png")

# Create Player Control Buttons
back_btn = Button(root, image=back_btn_img, borderwidth=0,bg="#EFE0BF",command=previous_song)
forward_btn = Button(root, image=foward_btn_img, borderwidth=0,bg="#EFE0BF",command=next_song)
play_btn = Button(root, image=play_btn_img, borderwidth=0,bg="#EFE0BF",command=play_song)
pause_btn = Button(root, image=pause_btn_img, borderwidth=0,bg="#EFE0BF",command=lambda: pause(paused))
stop_btn = Button(root, image=stop_btn_img, borderwidth=0,bg="#EFE0BF",command=stop)

# Place buttons individually
back_btn.place(x=320, y=450)
forward_btn.place(x=490, y=450)
play_btn.place(x=375, y=450)
pause_btn.place(x=435, y=450)
stop_btn.place(x=540, y=450)

# open folder - choose your song
Button(root,text="Your Playlist",width=25,height=1,font=("Arial",10,"bold"),fg="white",bg="#1E2647",command=open_folder).place(x=640,y=270)

# music
music_frame = Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=640,y=300,width=300,height=200)

# Create the label for the border
border_label = Label(root, bg="#EFE0BF", bd=2, relief="solid", width=40, height=5)
border_label.place(x=320, y=310)

# Create the label for the text "Now Playing..."
text_label = Label(root, text="Now Playing....", font=("arial", 10, "bold"), fg="black", bg="#EFE0BF")
text_label.place(x=320, y=280)
                  
# song name label after choosing song ("now playing")              
music=Label(root,text="",font=("arial",10,"bold"),fg="black",bg="#EFE0BF")
music.place(x=380,y=350,anchor="center")

# Music slider
style = ttk.Style()
style.theme_use('default')
style.configure("Horizontal.TScale", background="black", troughcolor="#EFE0BF")  # Set the background and trough color

# Create Music Position SLider
my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=290, style="Horizontal.TScale")
my_slider.place(x=320, y=410)

# Create Volume Slider
volume_slider = ttk.Scale(root, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=125)
volume_slider.place(x=280, y=300)

scroll = Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial",10),bg="#1E2647",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT,fill=BOTH)


root.mainloop()