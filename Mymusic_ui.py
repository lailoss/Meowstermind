import tkinter as tk

root = tk.Tk()
root.geometry("1200x700")
root.configure(bg="#1E2647")
frame_1=tk.Frame(root, width = 900, height=500, highlightbackground= 'blue',highlightthickness=20)
frame_1.pack(expand=True)

root.mainloop()
