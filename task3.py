import tkinter as tk 
from tkinter import *
from tkinter import ttk
window =tk.Tk()
window.title =("Task 3")
dogphoto = PhotoImage(file="dog.png")
label1=tk.Label(window,image=dogphoto)
label2=tk.Label(window,text="Pochacco!")
label3=tk.Label(window,text="A cuddly little puppy! This is from the same\n creators who brough you Keropi and Kero Kero")
label1.grid(row=1,column=1,sticky=E)
label2.grid(row=1,column=2,sticky=W)
label3.grid(row=3,column=1,columnspan=2)

window.mainloop()

