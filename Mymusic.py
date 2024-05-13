from tkinter import*
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os
import time
from mutagen.mp3 import MP3
import customtkinter
import pygame

music_window = customtkinter.CTk()
music_window.title("Meow Music")
music_window.geometry("800x500")
music_window.resizable(False,False)

# Initialise Pygame Mixer
pygame.mixer.init()

current_song_index = 0  # Global variable to store the current song index

def open_folder():
    songs = filedialog.askopenfilenames(initialdir="C:/Users/Fawqan/Meowstermind/Songs", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    
    # Loop thru song list and insert into playlist
    for song in songs:
        # Extract just the file name without the full path
        song_name = os.path.basename(song)
        # Insert the song name into the playlist
        playlist.insert(END, song_name)
   
# Grab song lenght time info
def play_time():
    # Check for double timing
    if stopped :
        return
    # Grab current song elapsed time
    current_time = pygame.mixer.music.get_pos() / 1000
    
    # throw up temporary label to get data
    #slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Pos :  {int(current_time)}')
    # Convert to time format
    converted_current_time = time.strftime('%H:%M:%S', time.gmtime(current_time))
    
    # Get currently playing song   
    current_song = playlist.curselection()
    # Grab song title from playlist
    song = playlist.get(current_song) # or put (ACTIVE) inside bracket if error
    # Add directory structure and mp3 to song title
    song = f'C:/Users/Fawqan/Meowstermind/Songs/{song}'
    # Load song length with mutagen
    song_mut =MP3(song)
    # Get song length
    global song_length
    song_length = song_mut.info.length
    # Convert To Time format
    converted_song_length = time.strftime('%H:%M:%S', time.gmtime(song_length))
    
    # Increase current time by 1 second
    current_time +=1
    
    if int(my_slider.get()) == int(song_length):
         # Output time to status bar
        status_bar.config(text=f'Time Elapsed: {converted_song_length}')
    
    elif paused :
        pass
    elif int(my_slider.get()) == int(current_time):
        # Slider hasnt been moved
        # Update slider to position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    else:
        # Slider HAS been Moved!
        
        # Update slider to position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))
        
        # Convert to time format
        converted_current_time = time.strftime('%H:%M:%S', time.gmtime(int(my_slider.get())))
        
        # Output time to status bar
        status_bar.config(text=f' {converted_current_time} of {converted_song_length}')
        
        # Move this thing along by one second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)
        
    # Output time to status bar
    #status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}')
    
    # Update Slider Position Value to current song position....
    #my_slider.config(value=int(current_time))
    
    # Update Time
    status_bar.after(1000, play_time)

    
# Play Button             
def play_song():
    # Get the selected song name from the playlist
    music_name = playlist.get(ACTIVE)
    # Set stopped variable to false so song can play
    global stopped
    stopped = False
    song = playlist.get(ACTIVE)
    
    # Load and play the selected song
    song_path = os.path.join("C:/Users/Fawqan/Meowstermind/Songs", song)  # Construct the full file path
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(loops=0)
    
    # Update the "Now Playing" label with just the song name
    music.config(text=music_name)
    
    # Call the play_time function to update the status bar
    play_time()

    
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
    # Reset Slider and Status bar
    status_bar.config(text='')
    my_slider.config(value=0)
    
    # Stop song from playing
    pygame.mixer.music.stop()
    playlist.selection_clear(ACTIVE)
    
    # Clear Status Bar
    status_bar.config(text='')
    
    # Set stop variable to true
    global stopped
    stopped = True
    
def previous_song():
    global current_song_index
    
    # Reset Slider and Status bar
    status_bar.config(text='')
    my_slider.config(value=0)

    # Decrement the current song index
    current_song_index -= 1
    
    # Check if the index goes below 0
    if current_song_index < 0:
        current_song_index = playlist.size() - 1  
    
    # Get the song title from the playlist using the current index
    song = playlist.get(current_song_index)
    song_path = f'C:/Users/Fawqan/Meowstermind/Songs/{song}'
    # Load and play the previous song
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(loops=0)
    
    # Update label with current song title
    music.config(text=song[0:-4])
    
    # Clear active bar in playlist listbox
    playlist.selection_clear(0, END)
    
    # Activate the new song bar
    playlist.activate(current_song_index)
    
    # Set Active bar to next song
    playlist.selection_set(current_song_index, last=None)
 
def next_song():
    # Reset Slider and Status bar
    status_bar.config(text='')
    my_slider.config(value=0)
    
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
    
# Delete A song
def delete_song():
    stop()
    # Delete currently selected song
    playlist.delete(ANCHOR)
    # Stop music if its play
    pygame.mixer.music.stop()
    
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

# Load the background image
bg_image = tk.PhotoImage(file="mymusicbg.png")

# Create a label with the background image and add it to the root window
bg_label = tk.Label(music_window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

inner_frame_width = 730
inner_frame_height = 383
inner_frame = customtkinter.CTkFrame(music_window, width=inner_frame_width, height=inner_frame_height, corner_radius=5, fg_color="#EFE0BF")
inner_frame.place(relx=0.5, rely=0.6, anchor=CENTER)

# font and title
font1 = ('Georgia',51,'bold')
title_label = customtkinter.CTkLabel(music_window,font=font1,text='Meow Music',text_color='#EFE0BF',bg_color='#1E2647')
title_label.place(x=150,y=50)

# button
# Define Player Control Button Images
back_btn_img = PhotoImage(file="back.png")
foward_btn_img = PhotoImage(file="foward.png")
play_btn_img = PhotoImage(file="play.png")
pause_btn_img = PhotoImage(file="pause.png")
stop_btn_img = PhotoImage(file="stop.png")

# Create Player Control Buttons with custom background color
back_btn = Button(music_window, image=back_btn_img, borderwidth=0, bg="#EFE0BF", command=previous_song)
forward_btn = Button(music_window, image=foward_btn_img, borderwidth=0, bg="#EFE0BF", command=next_song)
play_btn = Button(music_window,text="PLAY",width=10,height=1,font=("Arial",8,"bold"),fg="white",bg="#1E2647", command=play_song)
pause_btn = Button(music_window, image=pause_btn_img, borderwidth=0, bg="#EFE0BF", command=lambda: pause(paused))
stop_btn = Button(music_window, image=stop_btn_img, borderwidth=0, bg="#EFE0BF", command=stop)


# Place buttons individually
back_btn.place(x=90, y=355)
forward_btn.place(x=270, y=355)
play_btn.place(x=60, y=190)
pause_btn.place(x=180, y=355)
stop_btn.place(x=330, y=355)

# Button open folder - choose your song
Button(music_window,text="Your Playlist",width=19,height=1,font=("Arial",8,"bold"),fg="white",bg="#506580",command=open_folder).place(x=460,y=190)

# Button Remove song button
Button(music_window,text="Remove Song",width=19,height=1,font=("Arial",8,"bold"),fg="white",bg="#506580",command = delete_song).place(x=610,y=190)

# playlist frame
music_frame = Frame(music_window,bd=2,relief=RIDGE)
music_frame.place(x=460,y=220,width=300,height=200)

# Create the label for the border
border_label = Label(music_window, bg="#EFE0BF", bd=2, relief="solid", width=50, height=5)
border_label.place(x=60, y=229)

# Create the label for the text "Now Playing..."
text_label = Label(music_window, text="Now Playing....", font=("Georgia", 8, "bold"), fg="black", bg="#EFE0BF")
text_label.place(x=64, y=235)

# song name label display after choosing song ("now playing")              
music=Label(music_window,text="",font=("Georgia",12,"bold"),fg="black",bg="#EFE0BF")
music.place(x=228,y=270,anchor="center")

# Text for +
text_label2 = Label(music_window, text="+", font=("arial", 15, "bold"), fg="black", bg="#EFE0BF")
text_label2.place(x=400, y=165)

# Text for -
text_label3 = Label(music_window, text="-", font=("arial", 18, "bold"), fg="black", bg="#EFE0BF")
text_label3.place(x=380, y=160)

# Text for "VOLUME"
text_label3 = Label(music_window, text="volume", font=("arial", 8, "bold"), fg="black", bg="#EFE0BF")
text_label3.place(x=218, y=169)

# Time Minute and Sec of the song
status_bar = Label(music_window, text='',font=("Courier new",8,"bold"),fg="black",bg="#EFE0BF")
status_bar.place(x=265, y=316)

# Music slider 
music_slider_style = ttk.Style()
music_slider_style.theme_use('default')
music_slider_style.configure("Music.Horizontal.TScale", background="#506580", troughcolor="black",borderwidth=-2)  

# Create Music Position Slider
my_slider = ttk.Scale(music_window, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=355, style="Music.Horizontal.TScale")
my_slider.place(x=60, y=340)


# Volume slider style
volume_slider_style = ttk.Style()
volume_slider_style.theme_use('default')
volume_slider_style.configure("Volume.Horizontal.TScale", background="#1E2647", troughcolor="#899CB4")  

# Create Volume Slider
volume_slider = ttk.Scale(music_window, from_=0, to=1, orient=HORIZONTAL, value=1, command=volume, length=200, style="Volume.Horizontal.TScale")
volume_slider.place(x=218, y=195)

scroll = Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial",10),bg="#1E2647",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT,fill=BOTH)


music_window.mainloop()