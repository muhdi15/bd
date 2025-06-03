# File: login.py

import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient

class LoginWindow(ttk.Frame):
    def __init__(self, parent, on_success_callback):
        super().__init__(parent)
        self.parent = parent
        self.on_success_callback = on_success_callback
        self.pack(fill='both', expand=True)

        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["inventory_db"]
        self.users = self.db["users"]

        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        login_frame = ttk.Frame(self, padding=30)
        login_frame.place(relx=0.5, rely=0.5, anchor='center')

        ttk.Label(login_frame, text="Login", font=('Segoe UI', 24)).grid(column=0, row=0, columnspan=2, pady=10)

        ttk.Label(login_frame, text="Username:").grid(column=0, row=1, sticky='w', pady=5)
        self.username_entry = ttk.Entry(login_frame, width=30)
        self.username_entry.grid(column=1, row=1)

        ttk.Label(login_frame, text="Password:").grid(column=0, row=2, sticky='w', pady=5)
        self.password_entry = ttk.Entry(login_frame, show="*", width=30)
        self.password_entry.grid(column=1, row=2)

        login_btn = ttk.Button(login_frame, text="Login", command=self.login)
        login_btn.grid(column=0, row=3, columnspan=2, pady=15)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        user = self.users.find_one({"username": username, "password": password})
        if user:
            messagebox.showinfo("Login", f"Selamat datang, {username}")
            self.on_success_callback(user)
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah")

