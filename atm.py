from tkinter import *
from tkinter import messagebox

class ATM:
    def __init__(self, window):
        self.window = window
        self.window.title("ATM")
        self.window.geometry("500x500")

        self.pin = "7707"
        self.balance = 5000

    def loginScreen(self):
        Label(self.window,
              text="ATM",
              font=("Arial", 25, "bold")
              ).pack(pady=30)
        
        Label(self.window,
              text="Enter PIN:").pack()
        
        self.pinEntry = Entry(self.window, show="*")
        self.pinEntry.pack()

        Button(self.window, text="Login", command=self.login).pack()

    def login(self):
        pin = self.pinEntry.get()

        if pin == self.pin:
            pass
        else:
            messagebox.showwarning("Warning", "PIN is wrong, try again.")