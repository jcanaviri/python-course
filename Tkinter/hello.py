import tkinter as tk

from tkinter import ttk

window = tk.Tk()

window.geometry('600x400')
window.title('Hello World')

window.iconbitmap('icono.ico')

# Event of the button
def show_message():
    btn1.config(text='You make click')
    # Create a new element
    btn2 = ttk.Button(window, text='New btn')
    btn2.pack()

# Add a button
btn1 = ttk.Button(window, text='Click', command=show_message)
btn1.pack()

window.mainloop()
