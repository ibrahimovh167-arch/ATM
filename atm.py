from tkinter import *
from tkinter import messagebox

class ATM:
    def __init__(self, window):
        self.window = window
        self.window.title("ATM")
        self.window.geometry("500x500")

        self.pin = "7707"
        self.balance = 5000

        self.loginScreen()

    def loginScreen(self):
        self.clearScreen()

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
            self.mainScreen()
        else:
            messagebox.showwarning("Warning", "PIN is wrong, try again.")

    def mainScreen(self):
        self.clearScreen()

        Label(self.window, 
              text="ATM MENU",
              font=("Arial", 25, "bold")
              ).pack(pady=30)
        
        Button(self.window,
               text="Show balance",
               width=20,
               command=self.showBalance
               ).pack(pady=5)
        
        Button(self.window,
               text="Withdraw",
               width=20,
               command=self.withdraw
               ).pack(pady=5)
        
        Button(self.window,
               text="Deposit",
               width=20,
               command=self.deposit
               ).pack(pady=5)
        
        Button(self.window,
               text="Exit",
               width=20,
               command=self.window.destroy
               ).pack(pady=20)
        
    def showBalance(self):
        messagebox.showinfo("Info", f"Balance: {self.balance} AZN")

    def withdraw(self):
        amount = self.getAmount()

    def deposit(self):
        amount = self.getAmount()

    def getAmount(self):
        window = Toplevel(self.window)
        window.title("Operation")
        window.geometry("250x250")

        Label(window, text="Enter amount:").pack(pady=10)

        entry = Entry(window)
        entry.pack()

        result = []

        def confirmOperation():
            try:
                amount = float(entry.get())

                if amount <= 0:
                    raise ValueError
                
                result.append(amount)
                window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Enter true amount.")

        Button(window, text="OK", command=confirmOperation).pack(pady=10)

        window.grab_set()
        self.window.wait_window(window)

        if result:
            return result[0]
        
        return None
    
    def clearScreen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

window = Tk()
app = ATM(window)
window.mainloop()