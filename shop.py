from tkinter import *

store=Tk()
store.geometry ('800x500')
store.title('store by itang')
store_bg=PhotoImage(file='shop_bg.png')
storebg=Label(store, image=store_bg)
storebg.pack()

dark_green='#208135'
light_green='#91BF7F'














#backgrounds buttons
buybutton_bga=Button(store, text='BUY',font='comfortaa 10 bold', bg=dark_green, bd=0)
buybutton_bga.place(x=55,y=225)
usebutton_bga=Button(store, text='USE',font='comfortaa 10 bold', bg=light_green, bd=0)
usebutton_bga.place(x=155,y=225)

buybutton_bgb=Button(store, text='BUY',font='comfortaa 10 bold', bg=dark_green, bd=0)
buybutton_bgb.place(x=325,y=225)
usebutton_bgb=Button(store, text='USE',font='comfortaa 10 bold', bg=light_green, bd=0)
usebutton_bgb.place(x=425,y=225)

buybutton_bgc=Button(store, text='BUY',font='comfortaa 10 bold', bg=dark_green, bd=0)
buybutton_bgc.place(x=590,y=225)
usebutton_bgc=Button(store, text='USE',font='comfortaa 10 bold', bg=light_green, bd=0)
usebutton_bgc.place(x=700,y=225)

buybutton_bgd=Button(store, text='BUY',font='comfortaa 10 bold', bg=dark_green, bd=0)
buybutton_bgd.place(x=590,y=439)
usebutton_bgd=Button(store, text='USE',font='comfortaa 10 bold', bg=light_green, bd=0)
usebutton_bgd.place(x=700,y=439)

buybutton_bge=Button(store, text='BUY',font='comfortaa 10 bold', bg=dark_green, bd=0)
buybutton_bge.place(x=315,y=439)
usebutton_bge=Button(store, text='USE',font='comfortaa 10 bold', bg=light_green, bd=0)
usebutton_bge.place(x=425,y=439)

store.mainloop()
store.update()