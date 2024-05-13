from tkinter import *
from tkinter import ttk
import sqlite3

# Database
connect = sqlite3.connect('nota.db')
cursor = connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS notes (title PRIMARY KEY, content TEXT)")
connect.commit()

# Parameters
yellow = '#FFBD59'

# Window
note = Tk()
note.title('ScratchPad')
note.geometry('800x500')

# Tabs
notebook = ttk.Notebook(note)
notebook.pack(fill='both', expand=True)

# Tab 1 - Add new note
tab1 = Frame(notebook)
notebook.add(tab1, text='Add New Note')

title_entry = Entry(tab1, width='45', font='comfortaa 17 bold', bd=0)
title_entry.pack(pady=10)

content_entry = Text(tab1, width=93, height=16, bd=0, font='arial,  11', undo=True)
content_entry.pack()

def add_note():
    title = title_entry.get()
    content = content_entry.get("1.0", "end-1c")
    note_save = "INSERT OR IGNORE INTO notes(title,content) VALUES (?, ?)"
    cursor.execute(note_save, (title, content))
    connect.commit()
    title_entry.delete(0, END)
    content_entry.delete('1.0', END)

save_button = Button(tab1, text='+', font='comfortaa 15 bold', bg='white', bd=0, command=add_note)
save_button.pack(pady=10)

# Tab 2 - Search and view note
tab2 = Frame(notebook)
notebook.add(tab2, text='Search and View Note')

search_text = Entry(tab2, bd=0, width='10', font=('comfortaa 12 bold'))
search_text.pack(pady=10)

def search():
    title = search_text.get()
    searchquery = "SELECT * FROM notes WHERE title=?"
    cursor.execute(searchquery, (title,))
    note1 = cursor.fetchone()
    if note1:
        content_entry.delete("1.0", END)
        content_entry.insert(END, note1[1])
    else:
        content_entry.delete("1.0", END)
        content_entry.insert(END, 'NOTE NOT FOUND')

search_button = Button(tab2, text="Search", font='comfortaa 12 bold', bg=yellow, bd=0, command=search)
search_button.pack(pady=10)

content_entry = Text(tab2, width=93, height=16, bd=0, font='arial,  11', undo=True)
content_entry.pack()

note.mainloop()