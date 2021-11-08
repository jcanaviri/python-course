import tkinter as tk

from tkinter import ttk, messagebox


class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x130")
        self.title("Login with Python")
        self.iconbitmap("py.ico")
        self.resizable(0, 0)  # No change the size

        # Grid config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._create_widgets()
    
    def _create_widgets(self):
        # Labels
        user_label = ttk.Label(self, text="User: ")
        pass_label = ttk.Label(self, text="Password: ")
        user_label.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        pass_label.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        ttk.Entry(
            self,
        )

        # Entries
        self.user_entry = ttk.Entry(self)
        self.pass_entry = ttk.Entry(self, show='*')
        self.user_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self.pass_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        # The Button
        btn = ttk.Button(self, text="Log In", command=self._login)
        btn.grid(row=3, column=0, columnspan=2)


    def _login(self):
        messagebox.showinfo(
            "Login data", f"user: {self.user_entry.get()}, pass: {self.pass_entry.get()}"
        )

if __name__ == '__main__':
    login = Login()
    login.mainloop()
