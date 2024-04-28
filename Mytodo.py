import customtkinter
from tkinter import *
from tkcalendar import*
from tkinter import messagebox

root = customtkinter.CTk()
root.title('To do list')
root.geometry('1200x700')
root.resizable(False,False)

def add_task():
    task = task_entry.get()
    if not task:
        messagebox.showerror('Error', 'Please enter a task.')
        return

    deadline = dl_entry.get()
    if not deadline or deadline == "mm/dd/yyyy":
        messagebox.showerror('Error', 'Please select a deadline.')
        return

    tasks_list.insert(0, f"{task} - Deadline: {deadline}")
    task_entry.delete(0, END)
    dl_entry.delete(0, END)
    save_tasks()

        
        
def remove_task():
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror('Error', 'Choose a task to delete')
        
def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = tasks_list.get(0,END)
        for task in tasks:
            f.write(task + "\n")
            
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                tasks_list.insert(0, task.strip())
    except FileNotFoundError:
        pass
    
def pick_date(event):
    global cal, date_window
    
    date_window = Toplevel(root)
    date_window.grab_set()
    date_window.title("Choose Date ")
    date_window.geometry('250x220+290+370')    
    cal = Calendar(date_window, selectmode="day", date_pattern="mm/dd/y")    
    cal.place(x=0, y=0)
    
    submit_btn = Button(date_window, text="Submit", command=grab_date)
    submit_btn.place(x=80, y=190)
    
def grab_date():
    dl_entry.delete(0, END)
    dl_entry.insert(0, cal.get_date())
    date_window.destroy()

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
font2 = ('Arial',10,'bold')
font3 = ('Arial',10,'bold')

title_label = customtkinter.CTkLabel(root,font=font1,text='Meow To-DO...',text_color='#E8D09C',bg_color='#792B14')
title_label.place(x=400,y=160)

# add and remove button
add_button = customtkinter.CTkButton(root,command=add_task,font=font2,text_color='#fff',text='Add Task', fg_color='#13643F',hover_color='#06911f',bg_color='#09112e',corner_radius=5,width=80)
add_button.place(x=300,y=250)

remove_button = customtkinter.CTkButton(root,command=remove_task,font=font3,text_color='#fff',text='Remove Task', fg_color='#96061c',hover_color='#AD130E',bg_color='#09112e',cursor='hand2',corner_radius=5,width=80)
remove_button.place(x=400,y=250)

# entry box
task_entry = customtkinter.CTkEntry(root,font=font2,text_color='#000',fg_color='white',border_color='white',width=600,height=30)
task_entry.place(x=300,y=290)

# list box
tasks_list = Listbox(root,width=85,height=10,font=font3)
tasks_list.place(x=300,y=340)

# Calendar entry
dl_label = Label(root, text="Select Deadline: ", bg="#E8D09C", fg="black", font=("Arial", 8))
dl_label.place(x=500, y=260)

dl_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#BDB7C6", font=("Arial", 8))
dl_entry.place(x=600, y=260, width=250)
dl_entry.insert(0, "mm/dd/yyyy")
dl_entry.bind("<1>", pick_date)

load_tasks()
root.mainloop()