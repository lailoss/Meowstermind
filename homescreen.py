from tkinter import *
#import customtkinter
root = Tk()
root.geometry("1200x700")
root.title("Home Screen")
root.configure(bg="#E8D09C")
root.resizable(False, False)

#BACKGROUND----------------------------------------------------------


#FUNCTIONS-----------------------------------------------------------
def redirect_todo():
    import Mytodo
    Mytodo.create_todo_window()
    return

def redirect_music():
    import Mymusic
    Mymusic.create_music_window()
    return

def redirect_timer():
    import pomodoro
    pomodoro.create_pom()


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_15 = ("Gill Sans MT", 15)


#WIDGETS and PACKING-------------------------------------------------
botframe=Frame(root, bg="#FFFFFF", padx=20, pady=20)
botframe.pack(side="bottom")

todo_button = Button(botframe, text="todo", bg= "#FFFFFF", command=redirect_todo)
todo_button.grid(row= 1, column= 1)

pomodoro_button = Button(botframe, text="timer", bg= "#FFFFFF", command=redirect_timer)
pomodoro_button.grid(row= 1, column= 2)

note_button = Button(botframe, text="notepad", bg= "#FFFFFF")
note_button.grid(row= 1, column= 3)

music_button = Button(botframe, text="song", bg="#FFFFFF")
music_button.grid(row= 1, column= 4)

flash_button = Button(botframe, text="flashcards", bg= "#FFFFFF")
flash_button.grid(row= 1, column= 5)


root.mainloop()