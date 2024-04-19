from tkinter import*
from tkcalendar import*

root = Tk()
root.geometry("500x400")
root.configure(background="#726782")



# Get the selected date when the user closes the calendar

def pick_date(event):
    global cal, date_window
    
    date_window = Toplevel()
    date_window.grab_set()
    date_window.title("Choose Date ")
    date_window.geometry('250x220+290+370')    
    cal = Calendar(date_window, selectmode="day", date_pattern="mm/dd/y")    
    cal.place(x=0, y=0)
    
    submit_btn = Button(date_window, text="Select", command=grab_date)
    submit_btn.place(x=80, y=190)
    
def grab_date():
    dob_entry.delete(0, END)
    dob_entry.insert(0, cal.get_date())
    date_window.destroy()
                                                        

# Create entry that will accept highlighted date

dob_label = Label(root, text="Highlight DATE : ", bg="#726782" , fg = "white", font=("yu gothic ui", 13 ,"bold"))
dob_label.place(x=20, y=160)

dob_entry = Entry(root, highlightthickness=0, relief=FLAT, bg="white", fg="#BDB7C6", font=("yu gothic ui", 12 ,"bold"))
dob_entry.place(x=160, y=160, width=255)
dob_entry.insert(0, "dd/mm/yyyy")
dob_entry.bind("<1>", pick_date)



root.mainloop()

