from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog


note=Tk()
note.title('PurrfectNotes')
note.geometry('800x500')
note.iconbitmap(r'C:\Users\USER\Projects\Meowstermind\notes.ico')
notesbg=PhotoImage(file=r'C:\Users\USER\Projects\Meowstermind\meowtes.png')
bg=Label(note, image=notesbg)
bg.pack()

#text box--------------------------------------------------------------------------
my_text=Text(note, width=87, height=15, font='arial,  11', undo=True)
my_text.place(x='50', y='177')

#add buttons--------------------------------------------------------------------------
def add_notes():
    my_text.delete('1.0')
    note.title(text='New Notes')
    
#def open_notes():
    my_text.delete('1.0', END) #deletes previous note
    text_file=filedialog.askopenfilename(initialdir='C:\Users\USER\Projects\Meowstermind\notes', title='Open Note', filetypes=(('Text Files', '*.txt')))
    name=text_file
    note.title(name+' meow')
    text_file=open(text_file,'r')
    object=text_file.read()
    my_text.insert(END, object)


#buttons---------------------------------------------------------------------
savenotes_button=Button(note, text='SAVE', bg='#FFBD59', font='comfortaa 19 bold', borderwidth=0)
savenotes_button.place(x='615',y='439')
addnotes_button=Button(note, text='NEW', bg='#FFBD59', font='comfortaa 19 bold', borderwidth=0)
addnotes_button.place(x='454',y='439')
delete_button=Button(note, text='DELETE', bg='#FFBD59', font='comfortaa 19 bold', borderwidth=0)
delete_button.place(x='250',y='439')
save_button=Button(note, text='OPEN', bg='#FFBD59', font='comfortaa 19 bold', borderwidth=0)
save_button.place(x='100',y='439')

#menu --------------------------------------------------------------------------------
menu= Menu(note)
note.configure(menu=menu)



note.mainloop()