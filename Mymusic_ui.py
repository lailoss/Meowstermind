from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title('Meow Music')
root.geometry("800x500")

# Initialise Pygame Mixer
pygame.mixer.init()

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
    current_song = song_box.curselection()
    # Grab song title from playlist
    song = song_box.get(current_song) # or put (ACTIVE) inside bracket if error
    # Add directory structure and mp3 to song title
    song = f'C:/Users/Fawqan/Meowstermind/Songs/{song}.mp3'
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
        status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}')
        
        # Move this thing along by one second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)
        
    # Output time to status bar
    #status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}')
    
    # Update Slider Position Value to current song position....
    #my_slider.config(value=int(current_time))
    
    # Update Time
    status_bar.after(1000, play_time)

# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir="Songs", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    
    # Strip out the directory info and .mp3 extension from the song name
    song = song.replace("C:/Users/Fawqan/Meowstermind/Songs/","")
    song = song.replace(".mp3","")
    
    # Add song to listbox
    song_box.insert(END, song)
  
# Add many songs to playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir="Songs", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    
    # Loop thru song list and replace directory infor and mp3
    for song in songs:
         song = song.replace("C:/Users/Fawqan/Meowstermind/Songs/","")
         song = song.replace(".mp3","")
         
         # Insert into playlist
         song_box.insert(END, song)
        
# Play selected song  
def play():
    # Set stopped variable to false so song can play
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    song = f'C:/Users/Fawqan/Meowstermind/Songs/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
    # Call the play_time function to get song playlist
    play_time()
    
    # Update slider to position
    #slider_position = int(song_length)
    #my_slider.config(to=slider_position, value=0) #value = 0 for the slider to start from the beginning when select other song
    
    # Get current Volume
    #current_volume = pygame.mixer.music.get_volume()
    #slider_label.config(text=current_volume * 100)
    
# Stop playing current song
global stopped
stopped = False
def stop():
    # Reset Slider and Status bar
    status_bar.config(text='')
    my_slider.config(value=0)
    # Stop song from playing
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    
    # Clear Status Bar
    status_bar.config(text='')
    
    # Setbstop variable to true
    global stopped
    stopped = True
 
# Play The Next Song In the Playlist   
def next_song():
    # Reset Slider and Status bar
    status_bar.config(text='')
    my_slider.config(value=0)
    
    # Get the current song tuple number
    next_one = song_box.curselection()
    # Add one to the current song number
    next_one = next_one[0]+1
    # Grab song title from playlist
    song = song_box.get(next_one)
    # Add directory structure and mp3 to song title
    song = f'C:/Users/Fawqan/Meowstermind/Songs/{song}.mp3'
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
    # Clear active bar in playlist listbox
    song_box.selection_clear(0, END)
    
    # Activate the new song bar
    song_box.activate(next_one)
    
    # Set Active bar to next song
    song_box.selection_set(next_one, last=None)
    
    # Activate new song bar
    song_box.activate(next_one)
    
def previous_song():
    # Reset Slider and Status bar
    status_bar.config(text='')
    my_slider.config(value=0)
    # Get the current song tuple number
    next_one = song_box.curselection()
    # Add one to the current song number
    next_one = next_one[0]-1
    # Grab song title from playlist
    song = song_box.get(next_one)
    # Add directory structure and mp3 to song title
    song = f'C:/Users/Fawqan/Meowstermind/Songs/{song}.mp3'
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
    # Clear active bar in playlist listbox
    song_box.selection_clear(0, END)
    
    # Activate the new song bar
    song_box.activate(next_one)
    
    # Set Active bar to next song
    song_box.selection_set(next_one, last=None)
    
    # Activate new song bar
    song_box.activate(next_one)
    
# Delete A song
def delete_song():
    stop()
    # Delete currently selected song
    song_box.delete(ANCHOR)
    # Stop music if its play
    pygame.mixer.music.stop()
    
# Delete All Songs from playlist
def delete_all_songs():
    stop()
    # Delete Sll Songs
    song_box.delete(0, END)
    # Stop music if its play
    pygame.mixer.music.stop()
    
    
    
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
    
# Create slider function
def slide(x):
    #slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
    song = song_box.get(ACTIVE)
    song = f'C:/Users/Fawqan/Meowstermind/Songs/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))
    
# Create Volume Function
def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())
    
    # Get current volume
    #current_volume = pygame.mixer.music.get_volume()
    #slider_label.config(text=current_volume * 100)

# Create master frame
master_frame = Frame(root)
master_frame.pack(pady=20)  

  
# Create Playlist Box
song_box = Listbox(master_frame, bg="black",fg="green",width=60, selectbackground="gray", selectforeground="black")
song_box.grid(row=0, column=0)

# Define Player Control Button Images
back_btn_img = PhotoImage(file="stop.png")
foward_btn_img = PhotoImage(file="play.png")
play_btn_img = PhotoImage(file="play.png")
pause_btn_img = PhotoImage(file="pause.png")
stop_btn_img = PhotoImage(file="stop.png")

# Create Player Control Frame
controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)

# Create Volume Label Frame
volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=20)

# Create Player Control Buttons
back_btn = Button(controls_frame, image= back_btn_img, borderwidth=0, command=previous_song)
foward_btn= Button(controls_frame, image= foward_btn_img, borderwidth=0, command=next_song)
play_btn = Button(controls_frame, image= play_btn_img, borderwidth=0, command=play)
pause_btn = Button(controls_frame, image= pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_btn = Button(controls_frame, image= stop_btn_img, borderwidth=0, command=stop)

back_btn.grid(row=0, column=0, padx=10)
foward_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command= add_song)

# Add many songs to playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command= add_many_songs)

"""def play():
    pygame.mixer.music.load("Songs/meow1.mp3")
    pygame.mixer.music.play(loops=0)
    
def stop():
    pygame.mixer.music.stop()
my_button = Button(root, text="Play Song", font=("Helvetica", 32), command=play)
my_button.pack(pady=20)

stop_button = Button(root, text="Stop", command=stop)
stop_button.pack(pady=20)"""

# Create Delete song menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label='Remove songs', menu=remove_song_menu)
remove_song_menu.add_command(label='Delete a song from playlist', command=delete_song)
remove_song_menu.add_command(label='Delete All songs from playlist', command=delete_all_songs)

# Create Status Bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create Music Position SLider
my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.grid(row=2, column=0, pady=10)

# Create Volume Slider
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=125)
volume_slider.pack(pady=10)

# Create Temporary Slider Label
#slider_label = Label(root, text="0")
#slider_label.pack(pady=10)

root.mainloop()
