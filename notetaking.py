
from customtkinter import*
from tkinter.messagebox import *
from tkinter.filedialog import *
from PIL import Image

note=CTk()
note.title('PurrfectNotes')
note.geometry('800x500')
note.iconbitmap(r'C:\Users\USER\Projects\Meowstermind\notes.ico')
notesbg=CTkImage(Image.open('meowtes.png'))
bg=CTkLabel(note, image=notesbg, text='', size='800x500')
bg.pack()

note.mainloop()

