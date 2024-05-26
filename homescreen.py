from tkinter import *
from PIL import Image, ImageTk
import pygame
import os
import random
import time
root = Tk()
root.geometry("1200x700")
root.title("Home Screen")
root.configure(bg="#E8D09C")
root.resizable(False, False)

'''# Initialize Pygame mixer
pygame.mixer.init()'''

# Load Pygame window
embed = Frame(root, width=700, height=400)
embed.pack()

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

pygame.init()
screen = pygame.display.set_mode((700, 400), pygame.SRCALPHA)
screen.fill((0, 0, 0, 0))  # Fill with black for transparency


#FUNCTIONS-----------------------------------------------------------

def quote(screen, images, images_id):
    if not images_id:
        images_id = list(images.keys())
        random.shuffle(images_id)  # Shuffle again when reusing the function / went through the loop
    img_id = images_id.pop(0)  # Get the first image index and remove it from the list
    img = images[img_id]  # Retrieve the image corresponding to the index
    screen.blit(img, (0, 0))
    pygame.display.flip()
    pygame.time.delay(1000)
    quote(screen, images, images_id)


'''def redirect_todo():
    import Mytodo
    Mytodo.create_todo_window()
    return

def redirect_music():
    import Mymusic
    Mymusic.create_music_window()
    return

def redirect_timer():
    import pomodoro
    create
    return'''


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_15 = ("Gill Sans MT", 15)


#WIDGETS and PACKING-------------------------------------------------

images = {
    0: pygame.image.load('Quotes/wp1.png'),
    1: pygame.image.load('Quotes/wp2.png'),
    2: pygame.image.load('Quotes/wp3.png'),
    3: pygame.image.load('Quotes/wp4.png'),
    4: pygame.image.load('Quotes/wp5.png'),
    5: pygame.image.load('Quotes/wp6.png'),
    6: pygame.image.load('Quotes/wp7.png'),
    7: pygame.image.load('Quotes/wp8.png'),
    8: pygame.image.load('Quotes/wp9.png'),
    9: pygame.image.load('Quotes/wp10.png')
}

images_id = list(images.keys())
random.shuffle(images_id) #shuffles before going into the quote func


#footer
botframe = Frame(root, bg="#FFFFFF", padx=20, pady=20)
botframe.pack(side="bottom")

todo_button = Button(botframe, text="todo", bg= "#FFFFFF")
todo_button.grid(row= 1, column= 1)

pomodoro_button = Button(botframe, text="timer", bg= "#FFFFFF")
pomodoro_button.grid(row= 1, column= 2)

note_button = Button(botframe, text="notepad", bg= "#FFFFFF")
note_button.grid(row= 1, column= 3)

music_button = Button(botframe, text="song", bg="#FFFFFF")
music_button.grid(row= 1, column= 4)

flash_button = Button(botframe, text="flashcards", bg= "#FFFFFF")
flash_button.grid(row= 1, column= 5)

root.after(100, quote, screen, images, images_id) #start displaying images after 1000ms (1s)

root.mainloop()