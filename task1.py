import tkinter as tk 
from tkinter import *
from tkinter import ttk

window=tk.Tk()
window.title("Task 1")
entry1 = tk.Entry(window,text="Entry widgets can be typed in")
label1 = tk.Label(window,text="x")
entry2=tk.Entry(window,text="")
button=tk.Button(window,text="=")
entry3=tk.Entry(window,text="")
entry1.grid(row = 1, column = 1)
label1.grid(row=1, column=2)
entry2.grid(row=1, column=3)
button.grid(row=1, column=4)
entry3.grid(row=1, column=5)
window.mainloop()
