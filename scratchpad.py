from tkinter import *
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
notesbg=PhotoImage(file="./images/meowtes1.png")
bg=Label(note, image=notesbg)
bg.pack()

#title-----------------------------------------------------------

title_entry=Entry(note, width='45', font='comfortaa 17 bold', bd=0)
title_entry.place(x='150', y='75')
content_entry=Text(note, width=93, height=16, bd=0, font='arial,  11', undo=True)
content_entry.place(x='22', y='125')
#add new notes--------------------------------------------------

def add_note():
    title_entry.delete(0, END)
    content_entry.delete('1.0', END)
    
save_button=Button(note, text='+', font='comfortaa 15 bold', bg='white', bd=0, command=add_note).place(x='270',y='10')
    
    
    
#save into mote-------------------------------------
def save_note():
    global title_entry
    title = title_entry.get()
    content = content_entry.get("1.0", "end-1c")
    note_save="INSERT OR IGNORE INTO notes(title,content) VALUES ('%s1','%s')" % (title, content)
    cursor.execute(note_save)
    connect.commit()
    
save_button=Button(note, text='SAVE', font='comfortaa 15 bold', bg=yellow, bd=0, command=save_note).place(x='525',y='440')
    
#edit current note----------------------
def edit_note():
    title = title_entry.get()
    content = content_entry.get("1.0", "end-1c")
    note_edit="UPDATE notes SET content='%s' where title='%s1'" % (content,title)
    cursor.execute(note_edit)
    connect.commit()
    
edit_button=Button(note, text='EDIT', font='comfortaa 15 bold', bg=yellow, bd=0, command=save_note).place(x='410',y='440')
    
#delete note-------------------------------------------------

def delete_note():
    title = title_entry.get()
    note_delete="DELETE FROM notes WHERE title='%s1'"%(title)
    cursor.execute(note_delete)
    connect.commit()
    
delete_button=Button(note, text='DELETE', font='comfortaa 15 bold', bg=yellow, bd=0, command=save_note).place(x='275',y='440')

def search_note():
    search_window=Toplevel()
    search_window.title('View My Files')
    search_window.geometry('500x300')
    search_window.resizable(False,False)
    filelist=Listbox(search_window, font=('comfortaa 12 bold'))
    
    cursor.execute("SELECT * FROM notes")
    t=cursor.fetchall()
    for title in t:
        filelist.insert(END, title)
    cursor.execute("SELECT * FROM notes")
    t=cursor.fetchall()
    for title in t:
        print(title)
     
        
searchicon=PhotoImage(file='./images/search_icon.png')
search_button=Button(note, image=searchicon, font='comfortaa 16 bold', bg='white', bd=0, command=search_note).place(x='25',y='10')


note.mainloop()