from tkinter import *
root = Tk()
root.geometry("950x500")
root.title("Login Page")

#widgets
login_title = Label(root, text="Login")
username_label = Label(root, text="Username")
username_entry = Entry(root)
username_entry.get()
password_label = Label(root, text="Password")
password_entry = Entry(root, show="*")
password_entry.get()
login_button = Button(root, text="Login")

#pack it in
login_title.grid(row=0, column=0, columnspan=3, sticky="ew")
username_label.grid(row=1, column=1)
username_entry.grid(row=1, column=2)
password_label.grid(row=2, column=1)
password_entry.grid(row=2, column=2)
login_button.grid(row=3, column=0, columnspan=3, sticky="ew")

root.mainloop()