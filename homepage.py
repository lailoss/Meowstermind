from tkinter import *
root = Tk()

#background image
backgroundimage= PhotoImage(file = "bg_1_default.png")
canvas= Canvas(root, width=backgroundimage.width(), height=backgroundimage.height())
canvas.pack()
canvas.create_image(0,0, anchor=NW, image= backgroundimage)


#important loop-----------------------
root.mainloop()