from tkinter import *
root = Tk()
#root.geometry("1920x1080")

#background image
canvas= Canvas(root, width=192, height="108")
canvas.pack()
canvas.create_image(0,0, image= PhotoImage(file= "#3 bedroom.#3 bedroom.jpg"))

#important loop-----------------------
root.mainloop()