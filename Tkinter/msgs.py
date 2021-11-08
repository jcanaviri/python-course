import sys
import tkinter as tk

from tkinter import ttk, messagebox, Menu

window = tk.Tk()
window.geometry('600x400')
window.title('Using entry in tkinter')
window.iconbitmap('icono.ico')

input1 = ttk.Entry(window, width=30)
input1.grid(row=0, column=0)


def send():
    btn1.config(text=input1.get())
    msg = input1.get()

    if msg:
        messagebox.showinfo('Message title', f'Message content { msg }')

def close_window():
    window.quit()
    window.destroy()
    sys.exit()

def create_menu():
    """Settings for the main menu"""
    main_menu = Menu()
    sub_menu = Menu(main_menu, tearoff=False)
    sub_menu.add_command(label='New')
    sub_menu.add_separator()
    sub_menu.add_command(label='Close', command=close_window)
    main_menu.add_cascade(menu=sub_menu, label='File')

    help_menu = Menu(main_menu, tearoff=False)
    help_menu.add_command(label='About us')
    main_menu.add_cascade(menu=help_menu, label='Help')

    window.config(menu=main_menu)

btn1 = ttk.Button(window, text='send', command=send)
btn1.grid(row=0, column=1)

create_menu()

window.mainloop()
