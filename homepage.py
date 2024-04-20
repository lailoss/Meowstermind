from tkinter import *
root = Tk()
#root.geometry("1920x1080")

#background image
canvas= Canvas(root, width=1920, height="1080")
canvas.pack()
backgroundimage= PhotoImage(file = "bg_3_bedroom.jpg")
canvas.create_image(0,0, image= backgroundimage)

#important loop-----------------------
root.mainloop()