import customtkinter
from tkinter import *
from tkinter import messagebox

root = customtkinter.CTk()
root.title('To do list')
root.geometry('1200x700')


# background image
bg_image = PhotoImage(file="bg.png")
background_label = Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# outer frame
outer_frame_width = 800
outer_frame_height = 500
outer_frame = customtkinter.CTkFrame(root, width=outer_frame_width, height=outer_frame_height,corner_radius= 10 ,fg_color="#792B14")
outer_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# inner frame
inner_frame_width = 700
inner_frame_height = 350
inner_frame = customtkinter.CTkFrame(outer_frame, width=inner_frame_width, height=inner_frame_height, corner_radius=5, fg_color="#E8D09C")
inner_frame.place(relx=0.5, rely=0.6, anchor=CENTER)

image = PhotoImage(file="layingcat.png").subsample(3)

logo_label = Label(outer_frame, image=image, bg='#792B14')  # Set the background color to match the outer frame
logo_label.place(x=10, y=-4)

# font and title
font1 = ('Arial',50,'bold')
font2 = ('Arial',18,'bold')
font3 = ('Arial',10,'bold')

title_label = customtkinter.CTkLabel(root,font=font1,text='Meow To-DO...',text_color='#E8D09C',bg_color='#792B14')
title_label.place(x=400,y=160)

add_button = customtkinter.CTkButton(root,font=font2,text_color='#fff',text='Add Task', fg_color='#13643F',hover_color='#06911f',bg_color='#09112e',corner_radius=5,width=120)
add_button.place(x=300,y=250)


root.mainloop()