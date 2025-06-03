# File: main.py

import ttkbootstrap as tb
from tkinter import messagebox
from login import LoginWindow
from inventory import InventoryDashboard

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Inventaris Barang")
        self.root.geometry("1200x700")
        self.root.resizable(False, False)

        # Awal mulai dengan login window
        self.show_login()

    def show_login(self):
        self.login_frame = LoginWindow(self.root, self.on_login_success)

    def on_login_success(self, user_data):
        self.user_data = user_data
        self.login_frame.destroy()
        self.show_dashboard()

    def show_dashboard(self):
        self.dashboard = InventoryDashboard(self.root, self.user_data)

if __name__ == "__main__":
    app = tb.Window(themename="darkly")
    MainApp(app)
    app.mainloop()
