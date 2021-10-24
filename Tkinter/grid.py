import tkinter as tk

from tkinter import ttk  # Is a module that brings user interface components


window = tk.Tk()

window.geometry('600x400')
window.title('Using the grid of tkinter')
window.iconbitmap('icono.ico')

# Grid config
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=5)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=5)

def event1():
    btn1.config(text='Button 1 pressed')
def event2():
    btn2.config(text='Button 2 pressed')

def event4():
    btn4.config(text='Button 4 pressed', fg='blue', bg='yellow', relief=tk.GROOVE)

btn1 = ttk.Button(window, text='Button 1', command=event1)
btn1.grid(row=0, column=0, sticky='NSWE', 
    padx=40, pady=40, ipadx=20, ipady=50, columnspan=2, rowspan=2)

btn2 = ttk.Button(window, text='Button 2', command=event2)
# btn2.grid(row=1, column=0, sticky='NSWE')

btn3 = ttk.Button(window, text='Button 3')
# btn3.grid(row=0, column=1, sticky='NSWE')

btn4 = tk.Button(window, text='Button 4', command=event4)
# btn4.grid(row=1, column=1, sticky='NSWE')

window.mainloop()
