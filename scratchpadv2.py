from tkinter import *
from tkinter import ttk
import sqlite3


#database
connect=sqlite3.connect('nota.db')
cursor=connect.cursor() #allow you to send SQL commands to database
cursor.execute("CREATE TABLE IF NOT EXISTS notes (title PRIMARY KEY, content TEXT)")
connect.commit()

#parameters-------------------------------------------------
yellow='#FFBD59'

#window-------------------------------------------------------
note=Tk()
note.title('ScratchPad')
note.geometry('800x500')



#tabs------------------------------------------------------------------------------
notebook=ttk.Notebook(note)
notebook.pack(fill='both', expand=True)

tab1=Frame(notebook)
notebook.add(tab1,text='ADD NEW NOTES')






tab2=Frame(notebook)
notebook.add(tab2, text='VIEW MY NOTES')
notesbg1=PhotoImage(file="./images/meowtes2.png")
bg=Label(tab1, image=notesbg1)
bg.pack()
notesbg2=PhotoImage(file="./images/meowtes2.png")
bg2=Label(tab2, image=notesbg2)
bg2.pack()



#title-----------------------------------------------------------

title_entry=Entry(tab1, width='45', font='comfortaa 17 bold', bd=0)
title_entry.place(x='150', y='22')
content_entry=Text(tab1, width=93, height=16, bd=0, font='arial,  11', undo=True)
content_entry.place(x='29', y='80')

#add new notes--------------------------------------------------

def add_note():
    title_entry.delete(0, END)
    content_entry.delete('1.0', END)
    
save_button=Button(tab1, text='CLEAR', font='comfortaa 15 bold', bg=yellow , bd=0, command=add_note)
save_button.place(x='405',y='430')
    
#save into mote-------------------------------------
def save_note():
    global title_entry
    title = title_entry.get()
    content = content_entry.get("1.0", "end-1c")
    note_save="INSERT OR IGNORE INTO notes(title,content) VALUES (?,'?')" % (title, content)
    cursor.execute(note_save)
    connect.commit()
    
save_button=Button(tab1, text='SAVE', font='comfortaa 15 bold', bg=yellow, bd=0, command=save_note).place(x='550',y='430')
    
#edit current note----------------------
def edit_note():
    title = title_entry.get()
    content = content_entry.get("1.0", "end-1c")
    note_edit="UPDATE notes SET content='?' where title=?" % (content,title)
    cursor.execute(note_edit)
    connect.commit()
    
edit_button=Button(tab2, text='EDIT', font='comfortaa 15 bold', bg=yellow, bd=0, command=save_note).place(x='415',y='429')
    
#delete note-------------------------------------------------

def delete_note():
    title = title_entry.get()
    note_delete="DELETE FROM notes WHERE title=?"%(title)
    cursor.execute(note_delete)
    connect.commit()
    
delete_button=Button(tab2, text='DELETE', font='comfortaa 15 bold', bg=yellow, bd=0, command=save_note).place(x='520',y='429')
#search notes----------------------------------------------------------------------------

search_text= Entry(tab2, bd=0, width='10', font=('comfortaa 12 bold'))
search_text.place(x='150', y='25')

def search():
    global cursor
    title=search_text.get()
    searchquery="SELECT * FROM notes WHERE title=?"   
    cursor.execute(searchquery, (title,))
    note1=cursor.fetchone()
    if note1:
        content_entry.delete('1.0', END)
        content_entry.config(text=note1[1])
    else:
        content_entry.delete('1.0', END)
        content_entry.config(text='NOTE NOT FOUND')
        
searchicon=PhotoImage(file='./images/search_icon.png')

search_button=Button(tab2, image=searchicon, font='comfortaa 16 bold', bg='white', bd=0, command=search).place(x='740',y='25')

#tabs---------------------------------------------------------------------------------------------------

#--------------------------------------------------------
# style= ttk.Style()
# style.theme("notebook.Tab":{'padding':[10,3], 'font':('comfortaa', '5', 'bold')}
    
    
    
    

note.mainloop()

