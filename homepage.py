from tkinter import *
root = Tk()
#root.geometry("1920x1080")

#background image
backgroundimage= PhotoImage(file = "bg_3_bedroom.png")
canvas= Canvas(root, width=backgroundimage.width(), height=backgroundimage.height())
canvas.pack()
canvas.create_image(0,0, anchor=NW, image= backgroundimage)

#important loop-----------------------
root.mainloop()