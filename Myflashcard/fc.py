import sqlite3
import tkinter as tk
from tkinter import CENTER, ttk
from tkinter import messagebox
from ttkbootstrap import Style as ttkstyle
import customtkinter

root = tk.Tk()
root.title("Meow Flashcard")
root.geometry("800x500")
root.resizable(False,False)



def display_flashcards(cards):
    global card_index
    global current_cards
    
    card_index = 0
    current_cards = cards
    
    # Clear the display
    if not cards:
        clear_flashcard_display()
    else:
        show_card()
        
    show_card()
    
def clear_flashcard_display():
    word_label.config(text='')
    definition_label.config(text='')
# Function to display the current flashcards word
def show_card():
    global card_index
    global current_cards
    
    if current_cards:
        if 0 <= card_index < len(current_cards):
            word, _ = current_cards[card_index]
            word_label.config(text=word)
            definition_label.config(text='')
            
        else:
            clear_flashcard_display()
    else:
        clear_flashcard_display()
        
# Function to flip the current card and display its definition
def flip_card():
    global card_index
    global current_cards
    
    if current_cards:
        _, definition = current_cards[card_index]
        definition_label.config(text=definition)
        
# Function to move to the next card
def next_card():
    global card_index
    global current_cards
    
    if current_cards:
        card_index = min(card_index + 1, len(current_cards) -1)
        show_card()
        
# Function to move to the previous card
def prev_card():
    global card_index
    global current_cards
    
    if current_cards:
        card_index = max(card_index -1, 0)
        show_card()

# Load the background image
bg_image = tk.PhotoImage(file="pawbg.png")

# Create a label with the background image and add it to the root window
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# inner frame
inner_frame_width = 730
inner_frame_height = 383
inner_frame = customtkinter.CTkFrame(root, width=inner_frame_width, height=inner_frame_height, corner_radius=5, fg_color="#D4C9B5")
inner_frame.place(relx=0.5, rely=0.6, anchor=CENTER)

# font and title
font1 = ('Georgia',60,'bold')
title_label = customtkinter.CTkLabel(root,font=font1,text='MeowCards.',text_color='#874236',bg_color='#EFEDE0')
title_label.place(x=98,y=42)

 ## Initialize variables for tracking card index and current cards
card_index = 0
current_cards = []  # corrected variable name
    
# Label to display the word on flashcards
word_label = ttk.Label(root, text='', font=('TkDefaultFont', 24))
word_label.pack(padx=5, pady=40)
    
# Label to display the word on flashcard
definition_label = ttk.Label(root, text='', font=('TkDefaultFont', 16))
definition_label.pack(padx=5, pady=20)

# Button to flip the flashcard 
ttk.Button(root, text='Flip', command=flip_card).place(x=350,y=400)
    
# Button to view the next flashcard 
ttk.Button(root, text='Next', command=next_card).place(x=450,y=400)
    
# Button to view the previous flashcard 
ttk.Button(root, text='Previous', command=prev_card).place(x=250,y=400)
    


root.mainloop()