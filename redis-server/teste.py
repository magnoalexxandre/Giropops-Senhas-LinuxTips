import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Login App")

        self.email_label = tk.Label(self.master, text="Email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(self.master)
        self.email_entry.pack()

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.master, show='*')
        self.password_entry.pack()

        self.login_button = tk.Button(self.master, text="Login", command=self.on_login_button_click)
        self.login_button.pack()

    def on_login_button_click(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email == "" or password == "":
            messagebox.showerror("Error", "Please enter your email and password")
            return

        # Here you can validate the email and password
        # and navigate the user to the home page if the credentials are correct

root = tk.Tk()
app = LoginApp(root)
root.mainloop()