import sqlite3
import tkinter as tk
from tkinter import CENTER, ttk
from tkinter import messagebox
import customtkinter
from ttkbootstrap import Style as ttkstyle

root = tk.Tk()
root.title("Meow Flashcard")
root.geometry("800x500")
root.resizable(False,False)

# Functions

# Create Notebook widget inside the inner_frame
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Add a tab to the Notebook
tab1 = tk.Frame(notebook)
notebook.add(tab1, text='Create')

# Load the background image
bg_image = tk.PhotoImage(file="pawbg.png")

# Create a label with the background image and add it to the root window
bg_label = tk.Label(tab1, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# inner frame
inner_frame_width = 730
inner_frame_height = 383
inner_frame = customtkinter.CTkFrame(tab1, width=inner_frame_width, height=inner_frame_height, corner_radius=5, fg_color="#D4C9B5")
inner_frame.place(relx=0.5, rely=0.6, anchor=CENTER)

# font and title
font1 = ('Georgia',50,'bold')
title_label = customtkinter.CTkLabel(tab1,font=font1,text='MeowCards.',text_color='#874236',bg_color='#EFEDE0')
title_label.place(x=98,y=32)

# meowset frame
meowset_frame_width = 330
meowset_frame_height = 290
meowset_frame = customtkinter.CTkFrame(tab1, width=meowset_frame_width, height=meowset_frame_height, corner_radius=5, fg_color="#874236")
meowset_frame.place(x=410,y=140)

# Create the label for the text "Your Meowset" inside frame
your_meowset_label = customtkinter.CTkLabel(tab1, text="Your meowset :", font=("Arial", 15, "bold"),text_color='white' ,bg_color="#874236")
your_meowset_label.place(x=530, y=170)

# Set up variables for storing user input
set_name_var = tk.StringVar()
terms_var = tk.StringVar()
definition_var = tk.StringVar()

# Label and Entry Widgets for entering set name, word and definition

# set title :
set_name_label = customtkinter.CTkLabel(tab1, text="Set Tittle | Subject | Category :", font=("Canva Sans", 15),text_color='#746F66')
set_name_label.place(x=108, y=140)

entry_frame = tk.Frame(tab1, bg="#D4C9B5")
entry_frame.place(x=100, y=180)  # Adjust padx and pady as needed
entry = ttk.Entry(entry_frame, textvariable=set_name_var, width=31)
entry.pack(padx=7, pady=8)
entry.configure(background="#D4C9B5")

# set terms :
terms_label = customtkinter.CTkLabel(tab1, text="Terms :", font=("Canva Sans", 15),text_color='#746F66')
terms_label.place(x=175, y=230)

entry1_frame = tk.Frame(tab1, bg="#D4C9B5")
entry1_frame.place(x=100, y=260)  # Adjust padx and pady as needed
entry1 = ttk.Entry(entry1_frame, textvariable=terms_var, width=31)
entry1.pack(padx=7, pady=10)
entry1.configure(background="#D4C9B5")

# set definiton :
definition_label = customtkinter.CTkLabel(tab1, text="Definitions :", font=("Canva Sans", 15),text_color='#746F66')
definition_label.place(x=165, y=320)

entry2_frame = tk.Frame(tab1, bg="#D4C9B5")
entry2_frame.place(x=100, y=350)  # Adjust padx and pady as needed
entry2 = ttk.Entry(entry2_frame, textvariable=terms_var, width=31)
entry2.pack(padx=7, pady=10)
entry2.configure(background="#D4C9B5")

# Buttons 
# Button to add a word , command=add_word

add_word_button = ttk.Button(tab1, text='Add Word', style='AddWord.TButton', width=15)
add_word_button.place(x=100, y=415)

# Button to save the set ,command=create_set
save_set_button = ttk.Button(tab1, text='Save Set', style='SaveSet.TButton', width=15)
save_set_button.place(x=210, y=415)

# Button to select set card ,command=select_set
select_set_button = ttk.Button(tab1, text='SELECT', style='SaveSet.TButton', width=23)
select_set_button.place(x=418, y=300)

# Button to delete set card ,command=select_set
delete_set_button = ttk.Button(tab1, text='DELETE', style='SaveSet.TButton', width=23)
delete_set_button.place(x=580, y=300)

# Button to flashcard (fc) after select set ,command=
fc_set_button = ttk.Button(tab1, text='LEARN', style='SaveSet.TButton', width=50)
fc_set_button.place(x=418, y=350)

# select your card (box option)
sets_combobox = ttk.Combobox(tab1, state='readonly', width=45)
sets_combobox.place(x=425, y=210)

ttk.Style().configure("TButton", padding=6, relief="flat",background="#ADAAA1")

# Ensure bg color consistency for existing elements
title_label.configure(bg_color='#EFEDE0')
your_meowset_label.configure(bg_color="#874236")
set_name_label.configure(bg_color='#D4C9B5')
terms_label.configure(bg_color='#D4C9B5')
definition_label.configure(bg_color='#D4C9B5')

# Second Tab - Flashcards
tab2 = tk.Frame(notebook)
notebook.add(tab2, text='Flashcards')

# Load the background image
bg_image1 = tk.PhotoImage(file="pawbg1.png")

# Create a label with the background image and add it to the root window
bg_label = tk.Label(tab2, image=bg_image1)
bg_label.place(relwidth=1, relheight=1)

# inner frame
inner_frame_width = 730
inner_frame_height = 383
inner_frame = customtkinter.CTkFrame(tab2, width=inner_frame_width, height=inner_frame_height, corner_radius=5, fg_color="#D4C9B5")
inner_frame.place(relx=0.5, rely=0.6, anchor=CENTER)

# font and title
font1 = ('Georgia',50,'bold')
title_label = customtkinter.CTkLabel(tab2,font=font1,text='MeowCards.',text_color='#874236',bg_color='#EFEDE0')
title_label.place(x=98,y=32)

 ## Initialize variables for tracking card index and current cards
card_index = 0
current_cards = []  # corrected variable name
    
# Label to display the word on flashcards
word_label = ttk.Label(tab2, text='', font=('TkDefaultFont', 24))
word_label.place(x=200, y=200)
    
# Label to display the word on flashcard
definition_label = ttk.Label(tab2, text='', font=('TkDefaultFont', 16))
definition_label.place(x=200, y=300)

# Button to flip the flashcard , command=flip_card
ttk.Button(tab2, text='Flip').place(x=350,y=400)
    
# Button to view the next flashcard  , command=next_card
ttk.Button(tab2, text='Next').place(x=450,y=400)
    
# Button to view the previous flashcard  , command=prev_card
ttk.Button(tab2, text='Previous').place(x=250,y=400)



root.mainloop()