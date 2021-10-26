import tkinter as tk

from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Using entry in tkinter')
window.iconbitmap('icono.ico')

# widht es la cantidad de caracteres
# input1 = ttk.Entry(window, width=30, justify=tk.CENTER, show='*')
# input1 = ttk.Entry(window, width=30, justify=tk.CENTER, state=tk.DISABLED)
var1 = tk.StringVar(value='Default value')
input1 = ttk.Entry(window, width=30, textvariable=var1)

input1.grid(row=0, column=0)
# input1.insert(0, 'Introduce una cadena')
# input1.insert(tk.END, '.')
# input1.config(state='readonly')

def send():
    # btn1.config(text=input1.get())
    # input1.delete(0, tk.END)
    btn1.config(text=var1.get())
    var1.set('Change...')


btn1 = ttk.Button(window, text='send', command=send)
btn1.grid(row=0, column=1)

window.mainloop()
