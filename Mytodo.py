import customtkinter
from tkinter import *
from tkcalendar import*
from tkinter import messagebox
import tkinter as tk
import sqlite3

# Initialize SQLite database
conn = sqlite3.connect('tasks.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        deadline TEXT,
        category TEXT
    )
''')
conn.commit()

todo_window = customtkinter.CTk()
todo_window.title('meow todo?')
todo_window.geometry('800x500')
todo_window.resizable(False,False)

# add task functions [with deadline]
def add_task():
    task = task_entry.get()
    if not task:
        messagebox.showerror('Error', 'Please enter a task.')
        return

    deadline = dl_entry.get()
    if not deadline or deadline == "mm/dd/yyyy":
        messagebox.showerror('Error', 'Please select a deadline.')
        return

    category = category_var.get()  # Get the selected category from the dropdown menu
    if category == "Select Category":
        messagebox.showerror('Error', 'Please select a category.')
        return
    
    c.execute("INSERT INTO tasks (task, deadline, category) VALUES (?, ?, ?)", (task, deadline, category))
    conn.commit()
    
    task_id = c.lastrowid
    tasks_list.insert(END, f"{task_id}. {task} | Date: {deadline} | Category: {category}")
    
    task_entry.delete(0, END)
    dl_entry.delete(0, END)
    category_var.set("Select Category")  # Reset the dropdown menu
        
# remove task function     
def remove_task():
    selected = tasks_list.curselection()
    if selected:
        task_text = tasks_list.get(selected[0])
        task_id = int(task_text.split('.')[0])
        
        c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        
        tasks_list.delete(selected[0])
        
    else:
        messagebox.showerror('Error', 'Choose a task to delete')
        
def update_task_numbers(start_index):
    # Iterate through tasks after the deleted task
    for i in range(start_index, tasks_list.size()):
        # Extract the task text
        task_text = tasks_list.get(i)
        # Extract the task number
        task_number = int(task_text.split('.')[0])
        # Update the task number
        tasks_list.delete(i)
        tasks_list.insert(i, f"{task_number - 1}. {task_text.split('.', 1)[1]}")
        

# load tasks function
def load_tasks():
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    for task in tasks:
        task_id, task_text, deadline, category = task
        tasks_list.insert(END, f"{task_id}. {task_text} | Date: {deadline} | Category: {category}")

# calendar functions
def pick_date(event):
    global cal, date_window
    
    date_window = Toplevel(todo_window)
    date_window.grab_set()
    date_window.title("Choose Date ")
    date_window.geometry('250x220+290+370')    
    cal = Calendar(date_window, selectmode="day", date_pattern="mm/dd/y")    
    cal.place(x=0, y=0)
    
    submit_btn = Button(date_window, text="Select", command=grab_date)
    submit_btn.place(x=80, y=190)
    
def grab_date():
    dl_entry.delete(0, END)
    dl_entry.insert(0, cal.get_date())
    date_window.destroy()

# background image
bg_image = PhotoImage(file="todobg.png")
background_label = Label(todo_window, image=bg_image)

# Create a label with the background image and add it to the root window
bg_label = tk.Label(todo_window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Inner Frame
inner_frame_width = 730
inner_frame_height = 383
inner_frame = customtkinter.CTkFrame(todo_window, width=inner_frame_width, height=inner_frame_height, corner_radius=5, fg_color="#EFE0BF")
inner_frame.place(relx=0.5, rely=0.6, anchor=CENTER)


# font and title
font1 = ('Arial',50,'bold')
font2 = ('Arial',10,'bold')
font3 = ('Arial',10,'bold')

title_label = customtkinter.CTkLabel(todo_window,font=font1,text='Meow To-DO.',text_color='#EFE0BF',bg_color='#792B14')
title_label.place(x=60,y=40)

# add and remove button
add_button = customtkinter.CTkButton(todo_window,command=add_task,font=font2,text_color='#fff',text='Add Task', fg_color='#13643F',hover_color='#06911f',bg_color='#09112e',corner_radius=5,width=80)
add_button.place(x=80,y=140)

remove_button = customtkinter.CTkButton(todo_window,command=remove_task,font=font3,text_color='#fff',text='Remove Task', fg_color='#96061c',hover_color='#AD130E',bg_color='#09112e',cursor='hand2',corner_radius=5,width=80)
remove_button.place(x=170,y=140)

# dropdown menu for selecting the category
category_var = StringVar(todo_window)
category_var.set("Select Category")
category_menu = OptionMenu(todo_window, category_var,  "Personal", "Work", "Exam", "Event")
category_menu.config(font=("Arial", 8), bg="white", fg="#BDB7C6", highlightthickness=0, relief=FLAT)
category_menu.place(x=510, y=150, width=150, height= 20)

# entry box (insert task)
task_entry = customtkinter.CTkEntry(todo_window,font=font2,text_color='#000',fg_color='white',border_color='white',width=600,height=30)
task_entry.place(x=80,y=190)

# list box (display task , date , category)
tasks_list = Listbox(todo_window,width=85,height=10,font=font3)
tasks_list.place(x=80,y=240)

# Calendar entry (dl=deadline)
dl_label = Label(todo_window, text="Select Deadline: ", bg="#EFE0BF", fg="black", font=("Arial", 8))
dl_label.place(x=290, y=150)

dl_entry = Entry(todo_window, highlightthickness=0, relief=FLAT, bg="white", fg="#BDB7C6", font=("Arial", 8))
dl_entry.place(x=390, y=150, width=100, height=20)
dl_entry.insert(0, "mm/dd/yyyy")
dl_entry.bind("<1>", pick_date)

load_tasks()
todo_window.mainloop()