from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("1200x700")
root.title("Login Page")
root.configure(bg="#E8D09C")


#FUNCTIONS ---------------------------------------------------------
"""def login():
    username="meowstermind" #link db
    password="12345" #link db
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You shall pass.")
    else:
        messagebox.showerror(title="Error", message="You shall not pass.")"""


#FRAME---------------------------------------------------------------
frame=Frame(root, bg="#FFFFFF")

#to center frame
def center_frame(event=None):

    print("it works")
    bbox = root.bbox("all")  # get bounding box coordinates of all widgets
    screen_width = root.winfo_screenwidth()  #get screen width
    screen_height = root.winfo_screenheight()  #get screen height
    frame_width = bbox[2] - bbox[0] #frame.winfo_width() - get requested/recommended width
    frame_height = bbox[3] - bbox[1] #frame.winfo_height() - get requested/recommended height

    x = (screen_width - frame_width) // 2
    y = (screen_height - frame_height) // 2

    frame.config(width=frame_width, height=frame_height) 
    frame.place(x=x, y=y)


#PARAMETER-----------------------------------------------------------
font_30 = ("Gill Sans MT", 30, "bold")
font_15 = ("Gill Sans MT", 15)


#WIDGETS-------------------------------------------------------------
login_title = Label(frame, text="LOGIN", font=font_30ont30, padx=30, pady=30, bg="#FFFFFF")
username_label = Label(frame, text="Username", font=font_15ont15, padx=30, pady=15, bg="#FFFFFF")
username_entry = Entry(frame, font=font_15ont15, bg="#FFFFFF")
username_entry.get()
password_label = Label(frame, text="Password", font=font_15ont15, padx=30, pady=15, bg="#FFFFFF")
password_entry = Entry(frame, show="•", font=font_15ont15, bg="#FFFFFF")
password_entry.get()
login_button = Button(frame, text="Login", font=font_15ont15, pady=15, bg="#FFFFFF")


#pack it in
login_title.grid(row=0, column=0, columnspan=3, sticky="ew")
username_label.grid(row=1, column=1)
username_entry.grid(row=1, column=2)
password_label.grid(row=2, column=1)
password_entry.grid(row=2, column=2)
login_button.grid(row=3, column=0, columnspan=3, sticky="ew")

frame.pack(fill=BOTH, expand=True)
frame.pack_propagate(False)

root.bind("<Configure>", center_frame)
#frame.bind("<Configure>", center_frame)

root.mainloop()