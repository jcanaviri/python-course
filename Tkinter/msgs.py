import tkinter as tk

from tkinter import ttk, messagebox

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
        messagebox.showerror('Message title', f'Message content { msg }')
        messagebox.showwarning('Message title', f'Message content { msg }')


btn1 = ttk.Button(window, text='send', command=send)
btn1.grid(row=0, column=1)

window.mainloop()
