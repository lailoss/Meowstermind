import sqlite3
import tkinter as tk
from tkinter import CENTER, ttk
from tkinter import messagebox
import customtkinter
import sys
from ttkbootstrap import Style as ttkstyle

if len(sys.argv) < 2:
    print("Usage: python script.py <username>")
    sys.exit(1)

# Get the username from the command line arguments
username = sys.argv[1]

# Initialize SQLite database
conn = sqlite3.connect('database.db')

fc_window = tk.Tk()
fc_window.title("Meow Flashcard")
fc_window.geometry("800x500")
fc_window.resizable(False,False)

def switch_to_flashcards():
    notebook.select(tab2)
    
# Functions
# Create database tables if they don't exist
def create_tables(conn, username):
    cursor = conn.cursor()
    
    # Create flashcard_sets table
    cursor.execute(f''' 
        CREATE TABLE IF NOT EXISTS {username}_flashcard_sets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL   
        )                  
''')
    
    # Create flashcards table with foreign key reference to flashcard_sets
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {username}_flashcards(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            set_id INTEGER NOT NULL,
            word TEXT NOT NULL,
            definition TEXT NOT NULL,
            FOREIGN KEY (set_id) REFERENCES {username}_flashcard_sets(id)
        )
    ''')
    conn.commit()
    
    # Add a new flashcard set to the database
def add_set(conn, username, name):
        cursor = conn.cursor()
        
        # Insert the set name into flashcard_sets table
        cursor.execute(f'''
             INSERT INTO {username}_flashcard_sets(name)
             VALUES(?)      
        ''',(name,))
        
        set_id = cursor.lastrowid
        conn.commit()
        
        return set_id
  
# Function to add a flashcard to the database
def add_card(conn, username, set_id, word, definition):
    cursor = conn.cursor()
    
    # Execute SQL query to insert a new flashcard into the database
    cursor.execute(f''' 
         INSERT INTO {username}_flashcards (set_id, word, definition)
         VALUES (?, ?, ?)
    ''', (set_id, word, definition))
    
    # Get the ID of the newly inserted card
    card_id = cursor.lastrowid
    conn.commit()
    
    return card_id

# Function to retrieve all flashcard sets from the database
def get_sets(conn, username):
    cursor = conn.cursor()
        
    # Execite SQL query to fetch all flashcard sets
    cursor.execute(f''' 
        SELECT id, name FROM {username}_flashcard_sets
    ''')
        
    rows = cursor.fetchall()
    sets = {row[1]: row[0] for row in rows} # Create a dictionary of sets (name: id)
        
    return sets
    
# Function to retrieve all flashcards of a specific set
def get_cards(conn,username, set_id):
    cursor = conn.cursor()
    
    cursor.execute(f''' 
        SELECT word, definition FROM {username}_flashcards
        WHERE set_id = ?
    ''', (set_id,))
    
    rows = cursor.fetchall()
    cards = [(row[0], row[1]) for row in rows] # Create a list of cards (word, definition)
    
    return cards
        
# Function to delete a flashcard set from the database
def delete_set(conn, username, set_id):
    cursor = conn.cursor()
    
    # Execute SQL query to delete a flashcard set
    cursor.execute(f'''
        DELETE FROM {username}_flashcard_sets
        WHERE id = ?
    ''', (set_id,))
    
    conn.commit()
    sets_combobox.set('')
    clear_flashcard_display()
    populate_sets_combobox()
    
    # Clear the current_cards list and reset card_index
    global current_cards, card_index
    current_cards= []
    card_index = 0
    
# Function to create a new flashcard set
def create_set():
    set_name = set_name_var.get()
    if set_name:
        if set_name not in get_sets(conn, username):
            set_id = add_set(conn, username, set_name)
            populate_sets_combobox()
            set_name_var.set('')
            
            # Clear the input fields
            set_name_var.set('')
            terms_var.set('')
            definition_var.set('')
            select_set() # Refresh display after creating a new set
               
def add_word():
    set_name = set_name_var.get()
    word = terms_var.get()
    definition = definition_var.get()
    
    if set_name and word and definition:
        if set_name not in get_sets(conn, username):
            set_id = add_set(conn,username, set_name)
        else:
            set_id = get_sets(conn, username)[set_name]
            
        add_card(conn, username, set_id, word, definition)
        
        terms_var.set('')
        definition_var.set('')    
               
        populate_sets_combobox()  
        select_set() # Refresh display after adding a new word

def populate_sets_combobox():
    sets_combobox['values'] = tuple(get_sets(conn, username).keys())
    
# Function to delete a flashcard from the database
def delete_card(conn, card_id):
    cursor = conn.cursor()
    
    # Execute SQL query to delete a flashcard
    cursor.execute(f'''
        DELETE FROM {username}_flashcards
        WHERE id = ?
    ''', (card_id,))
    
    conn.commit()

# Function to edit a flashcard in the database
def edit_card(conn, card_id, new_word, new_definition):
    cursor = conn.cursor()
    
    # Execute SQL query to update the word and definition of a flashcard
    cursor.execute(f'''
        UPDATE {username}_flashcards
        SET word = ?, definition = ?
        WHERE id = ?
    ''', (new_word, new_definition, card_id))
    
    conn.commit()
    
# Function to delete a selected flashcard set
def delete_selected_set():
    set_name = sets_combobox.get()
    
    if set_name:
        result = messagebox.askyesno(
            'Confirmation', f'Are you sure you want to delete the "{set_name}" set?'
        )
        
        if result == tk.YES:
            set_id = get_sets(conn, username)[set_name]
            delete_set(conn, username, set_id)
            populate_sets_combobox()
            clear_flashcard_display()

# Function to edit a selected flashcard
def edit_selected_card():
    if current_cards:
        word, definition = current_cards[card_index]

        # Retrieve the set_id and the card_id
        set_name = sets_combobox.get()
        set_id = get_sets(conn, username).get(set_name)
        card_id_query = f'''SELECT id FROM {username}_flashcards WHERE set_id = ? AND word = ? AND definition = ?'''
        cursor = conn.cursor()
        cursor.execute(card_id_query, (set_id, word, definition))
        card_id = cursor.fetchone()[0]

        # Create a popup window to edit the flashcard
        edit_window = tk.Toplevel(fc_window)
        edit_window.title('Edit card')

        # Entry fields to edit the word and definition
        new_word_var = tk.StringVar(value=word)
        new_definition_var = tk.StringVar(value=definition)

        new_word_label = ttk.Label(edit_window, text='New Word:')
        new_word_entry = ttk.Entry(edit_window, textvariable=new_word_var)

        new_definition_label = ttk.Label(edit_window, text='New Definition:')
        new_definition_entry = ttk.Entry(edit_window, textvariable=new_definition_var)

        # Button to confirm changes, passing the card_id and card_index as well
        confirm_button = ttk.Button(edit_window, text='Confirm', 
                                    command=lambda: confirm_edit(edit_window, card_id, card_index, new_word_var.get(), new_definition_var.get()))

        new_word_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        new_word_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        new_definition_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        new_definition_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        confirm_button.grid(row=2, column=0, columnspan=2, pady=10)


def confirm_edit(edit_window, card_id, card_index, new_word, new_definition):
    global current_cards  # Declare current_cards as global here
    if current_cards:
        edit_card(conn, card_id, new_word, new_definition)
        edit_window.destroy()

        set_name = sets_combobox.get()
        if set_name:
            set_id = get_sets(conn, username).get(set_name)
            cards = get_cards(conn, username, set_id)

            # Update the display and keep the current card index
            current_cards = cards
            show_card_at_index(card_index)


def show_card_at_index(index):
    global card_index
    global current_cards

    card_index = index
    if current_cards:
        if 0 <= card_index < len(current_cards):
            word, _ = current_cards[card_index]
            word_label.config(text=word)
            definition_label.config(text='')
        else:
            clear_flashcard_display()
    else:
        clear_flashcard_display()

            
def delete_card_set():
    global current_cards, card_index, username
    set_name = sets_combobox.get()
    if set_name:
        set_id = get_sets(conn, username)[set_name]
        if current_cards:
            # Get the ID of the card to delete
            word, _ = current_cards[card_index]
            cursor = conn.cursor()
            cursor.execute(f'''
                SELECT id FROM {username}_flashcards
                WHERE set_id = ? AND word = ?
            ''', (set_id, word))
            card_id = cursor.fetchone()[0]

            # Delete the card
            delete_card(conn, card_id)
            
            # Refresh the card list
            current_cards = get_cards(conn, username, set_id)

            # Adjust card_index to point to the next card if available
            if card_index >= len(current_cards):
                card_index = max(0, len(current_cards) - 1)

            # Display the next card if available
            if current_cards:
                show_card()
            else:
                clear_flashcard_display()
                word_label.config(text="No cards in this set")
                definition_label.config(text='')

            
# LEARN button command
def learn_flashcards():
    switch_to_flashcards()
    select_set()
            
def select_set():
    set_name = sets_combobox.get()
    
    if set_name:
        set_id = get_sets(conn, username)[set_name]
        cards = get_cards(conn, username, set_id)
        
        if cards:
            display_flashcards(cards)
        else:
            word_label.config(text="No cards in this set")
            definition_label.config(text='')
            
    else:
        # Clear the current cards list and reset card index
        global current_cards, card_index
        current_cards = []
        card_index = 0
        clear_flashcard_display()

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
def flip_card(event=None):
    global card_index
    global current_cards

    if current_cards:
        _, definition = current_cards[card_index]
        definition_label.config(text=definition)
        
# Function to handle the space key press event
def handle_space(event):
    
    # Check if the focus is not on an entry widget before flipping the card
    if fc_window.focus_get() not in [entry, entry1, entry2]:
        flip_card
        
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


if __name__ == '__main__':
    # Connect to the SQLite database and create tables
    conn = sqlite3.connect('database.db')
    create_tables(conn, username)

# Create Notebook widget inside the inner_frame
notebook = ttk.Notebook(fc_window)
notebook.pack(fill='both', expand=True)

# Add a tab to the Notebook
tab1 = tk.Frame(notebook)
notebook.add(tab1, text='Create')

# Load the background image
bg_image = tk.PhotoImage(file="./images/pawbg.png")

# Create a label with the background image and add it to the fc_window window
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
entry2 = ttk.Entry(entry2_frame, textvariable=definition_var, width=31)
entry2.pack(padx=7, pady=10)
entry2.configure(background="#D4C9B5")

# Buttons 
# Button to add a word

add_word_button = ttk.Button(tab1, text='Add Word', style='AddWord.TButton', width=15 , command=add_word)
add_word_button.place(x=100, y=415)

# Button to save the set 
save_set_button = ttk.Button(tab1, text='Save Set', style='SaveSet.TButton', width=15,command=create_set)
save_set_button.place(x=210, y=415)

# Button to select set card 
select_set_button = ttk.Button(tab1, text='SELECT', style='SaveSet.TButton', width=23,command=select_set)
select_set_button.place(x=418, y=300)

# Button to delete set card ,command=select_set
delete_set_button = ttk.Button(tab1, text='DELETE', style='SaveSet.TButton', width=23, command=delete_selected_set)
delete_set_button.place(x=580, y=300)

# Button to flashcard (fc) after select set ,command=
fc_set_button = ttk.Button(tab1, text='START', style='SaveSet.TButton', width=50, command=learn_flashcards)
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
bg_image1 = tk.PhotoImage(file="./images/pawbg1.png")

# Create a label with the background image and add it to the fc_window window
bg_label = tk.Label(tab2, image=bg_image1)
bg_label.place(relwidth=1, relheight=1)

# inner frame
inner_frame_width = 730
inner_frame_height = 390
inner_frame = customtkinter.CTkFrame(tab2, width=inner_frame_width, height=inner_frame_height, corner_radius=5, fg_color='#45595A')
inner_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# flashcard frame
meowset_frame_width = 690
meowset_frame_height = 240
meowset_frame = customtkinter.CTkFrame(tab2, width=meowset_frame_width, height=meowset_frame_height, corner_radius=5, fg_color="#D4C9B5")
meowset_frame.place(x=50,y=100)

 ## Initialize variables for tracking card index and current cards
card_index = 0
current_cards = []  # corrected variable name
    
# Label to display the word on flashcards
word_label = ttk.Label(tab2, text=' ', font=('Georgia', 25), background="#D4C9B5", wraplength=meowset_frame_width - 40, anchor="center", justify="center")
word_label.place(x=170, y=150)  # Adjust the y-coordinate to make room for the definition label

# Label to display the definition on flashcard
definition_label = ttk.Label(tab2, text=' ', font=('Arial', 15), background="#D4C9B5", wraplength=meowset_frame_width - 30, anchor="center", justify="center")
definition_label.place(x=170, y=230)  # Adjust the y-coordinate to make room for the word label

# button
# Create PhotoImage objects for the images
flip_image = tk.PhotoImage(file='./images/flip.png')
next_image = tk.PhotoImage(file='./images/next.png')
prev_image = tk.PhotoImage(file='./images/pre.png')

# Create Player Control Buttons with custom background color and images
flip_btn = tk.Button(tab2, image=flip_image, command=flip_card, borderwidth=0, highlightthickness=0)
next_btn = tk.Button(tab2, image=next_image, command=next_card, borderwidth=0, highlightthickness=0)
pre_btn = tk.Button(tab2, image=prev_image, command=prev_card, borderwidth=0, highlightthickness=0)

# Set background color directly
flip_btn.configure(bg="#45595A")
next_btn.configure(bg="#45595A")
pre_btn.configure(bg="#45595A")

# Place buttons individually
flip_btn.place(x=350, y=355)
next_btn.place(x=470, y=355)
pre_btn.place(x=230, y=355)

fc_window.bind('<Up>', lambda event: (fc_window.focus_set(), flip_card()))
fc_window.bind('<Right>', lambda event: next_card())
fc_window.bind('<Left>', lambda event: prev_card())

# Modify your button creation to include buttons for editing and deleting flashcards
edit_flashcard_button = ttk.Button(tab2, text='Edit card', command=edit_selected_card)
edit_flashcard_button.place(x=50, y=60)

delete_flashcard_button = ttk.Button(tab2, text='Delete card', command=delete_card_set)
delete_flashcard_button.place(x=130, y=60)

populate_sets_combobox()
fc_window.mainloop()