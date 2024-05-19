from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import random
import time
root = Tk()
root.geometry("1200x700")
root.title("Home Screen")
root.configure(bg="#E8D09C")
root.resizable(False, False)


#FUNCTIONS-----------------------------------------------------------

def quote(canvas, images):
    for img_id, img in images.items():
        canvas.delete("all")
        x = random.randint(0, canvas.winfo_width() - img.width())
        y = random.randint(0, canvas.winfo_height() - img.height())
        canvas.create_image(x, y, anchor=NW, image=img)
        canvas.update()
        time.sleep(5)


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
quoteframe = Frame(root, width=700, height=400, bg="#FFFFFF")
quoteframe.pack(expand=True)
quoteframe.pack_propagate(False) #prevents resizing according to content / maintains size

canvas = Canvas(quoteframe, width=700, height=400, bg="#000000")
canvas.pack()

images = {
    0: ImageTk.PhotoImage(Image.open('Quotes/wp1.png')),
    1: ImageTk.PhotoImage(Image.open('Quotes/wp2.png')),
    2: ImageTk.PhotoImage(Image.open('Quotes/wp3.png')),
    3: ImageTk.PhotoImage(Image.open('Quotes/wp4.png')),
    4: ImageTk.PhotoImage(Image.open('Quotes/wp5.png')),
    5: ImageTk.PhotoImage(Image.open('Quotes/wp6.png')),
    6: ImageTk.PhotoImage(Image.open('Quotes/wp7.png')),
    7: ImageTk.PhotoImage(Image.open('Quotes/wp8.png')),
    8: ImageTk.PhotoImage(Image.open('Quotes/wp9.png')),
    9: ImageTk.PhotoImage(Image.open('Quotes/wp10.png'))
}


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

root.after(1000, quote, canvas, images) #start displaying images after 1000ms (1s)

root.mainloop()