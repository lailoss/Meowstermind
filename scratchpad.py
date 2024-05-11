from tkinter import *
import sqlite3

#database
connect=sqlite3.connect('notes.db')
cursor=connect.cursor() #allow you to send SQL commands to database
cursor.execute("CREATE TABLE IF NOT EXISTS notes (title PRIMARY KEY, content TEXT)")
connect.commit()

#parameters-------------------------------------------------
yellow='#FFBD59'

#window-------------------------------------------------------
note=Tk()
note.title('ScratchPad')
note.geometry('800x500')
notesbg=PhotoImage(file="./images/meowtes.png")
bg=Label(note, image=notesbg)
bg.pack()

#title-----------------------------------------------------------

title=Entry(note, width='45', font='comfortaa 17 bold', bd=0)
title.place(x='150', y='75')
content=Text(note, width=93, height=16, bd=0, font='arial,  11', undo=True)
content.place(x='22', y='125')
#add new notes--------------------------------------------------

def add_note():
    title=Entry(note, width='45', font='comfortaa 17 bold', bd=0)
    title.place(x='150', y='75')
    content=Text(note, width=93, height=16, bd=0, font='arial,  11', undo=True)
    content.place(x='22', y='125')
    
save_button=Button(note, text='+', font='comfortaa 15 bold', bg='white', bd=0, command=add_note).place(x='270',y='10')
    
    
    
#save into mote-------------------------------------
def save_note():
    note_add="INSERT INTO notes(title,content) values('%s1','%s')" % (title, content)
    cursor.execute(note_add)
    connect.commit()
    
save_button=Button(note, text='SAVE', font='comfortaa 15 bold', bg=yellow, bd=0, command=save_note).place(x='525',y='440')
    
#edit current note----------------------
def edit_note():
    note_edit="UPDATE notes SET content='%s' where title='%s1'" % (content,title)
    cursor.execute(note_edit)
    connect.commit()
    
edit_button=Button(note, text='EDIT', font='comfortaa 15 bold', bg=yellow, bd=0, command=save_note).place(x='410',y='440')
    
#delete note-------------------------------------------------

def delete_note():
    note_delete="DELETE FROM notes WHERE title='%s1'"%(title)
    cursor.execute(note_delete)
    connect.commit()
    
delete_button=Button(note, text='DELETE', font='comfortaa 15 bold', bg=yellow, bd=0, command=save_note).place(x='275',y='440')

def search_note():
    cursor.execute("SELECT * FROM notes")
    t=cursor.fetchall()
    for title in t:
        print(title)
        
searchicon=PhotoImage(file='./images/search_icon.png')
search_button=Button(note, image=searchicon, font='comfortaa 16 bold', bg='white', bd=0, command=search_note).place(x='25',y='10')


note.mainloop()
