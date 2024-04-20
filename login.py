from tkinter import *
root = Tk()
root.geometry("950x500")
root.title("Login Page")
root.configure(bg="#E8D09C")

#frame
frame= Frame(bg="#FFFFFF")

#widgets
login_title = Label(frame, text="Login", font=("Lato", 30), padx=30, pady=30, bg="#FFFFFF")
username_label = Label(frame, text="Username", font=("Lato", 15), padx=30, pady=15, bg="#FFFFFF")
username_entry = Entry(frame, font=("Lato", 15), bg="#FFFFFF")
username_entry.get()
password_label = Label(frame, text="Password", font=("Lato", 15), padx=30, pady=15, bg="#FFFFFF")
password_entry = Entry(frame, show="•", font=("Lato", 15), bg="#FFFFFF")
password_entry.get()
login_button = Button(frame, text="Login", font=("Lato", 15), pady=15, bg="#FFFFFF")


#pack it in
login_title.grid(row=0, column=0, columnspan=3, sticky="ew")
username_label.grid(row=1, column=1)
username_entry.grid(row=1, column=2)
password_label.grid(row=2, column=1)
password_entry.grid(row=2, column=2)
login_button.grid(row=3, column=0, columnspan=3, sticky="ew")

frame.pack()
root.mainloop()