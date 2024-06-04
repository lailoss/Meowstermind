from tkinter import *

info=Tk()
info.geometry('500x300')
info.title ('All About Meowstermind!')
info.resizable(False, False)
infobg=PhotoImage(file='meowstermindinfo.png')
bg=Label(info,image=infobg)
bg.pack()

info.mainloop()