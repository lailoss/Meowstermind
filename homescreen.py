from tkinter import *
#import customtkinter
root = Tk()
root.geometry("1200x700")
root.title("Home Screen")
root.configure(bg="#E8D09C")
root.resizable(False, False)

#BACKGROUND----------------------------------------------------------


#FUNCTIONS-----------------------------------------------------------

def quote():

    image = PhotoImage(file="cuba.png")

    image_label = Label(midframe, image=image)
    image_label.image = image  # prevents garbage collection
    image_label.grid(row=0, column=1)


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
midframe = Frame(root, padx=20, pady=20, bg="#FFFFFF")
midframe.pack(expand=True)

quote = Button(midframe, text="quote", fg="navy", relief="flat", command=quote)
quote.grid(row=0, column=0)

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


root.mainloop()