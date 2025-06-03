# File: inventory.py

import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from db import get_db
from transactions import TransactionWindow
from categories import CategoryWindow
from reports import ReportWindow
from tkinter import messagebox

class InventoryDashboard(ttk.Frame):
    def __init__(self, parent, user_data):
        super().__init__(parent)
        self.parent = parent
        self.user_data = user_data
        self.db = get_db()
        self.items = self.db['items']
        self.init_ui()

    def init_ui(self):
        self.pack(fill='both', expand=True)

        self.sidebar = ttk.Frame(self, width=200, padding=10)
        self.sidebar.pack(side='left', fill='y')

        self.main_area = ttk.Frame(self, padding=10)
        self.main_area.pack(side='right', expand=True, fill='both')

        ttk.Label(self.sidebar, text="Inventaris", font=('Segoe UI', 18)).pack(pady=(0,20))

        self.nav_buttons = [
            ("Barang", self.show_items),
            ("Barang Masuk/Keluar", self.show_transactions),
            ("Kategori", self.show_categories),
            ("Laporan", self.show_reports),
            ("Logout", self.logout)
        ]

        for name, cmd in self.nav_buttons:
            btn = ttk.Button(self.sidebar, text=name, command=cmd, width=20)
            btn.pack(pady=5)

        ttk.Label(self.sidebar, text=f"Login sebagai:\n{self.user_data['username']} ({self.user_data['role']})",
                  font=('Segoe UI', 10), foreground='gray').pack(side='bottom', pady=10)

        self.show_items()

    def show_items(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()

        ttk.Label(self.main_area, text="Daftar Barang", font=('Segoe UI', 16)).pack(anchor='w')

        columns = ("Nama", "Kategori", "Jumlah", "Kondisi")
        self.tree = ttk.Treeview(self.main_area, columns=columns, show='headings', height=20)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200)
        self.tree.pack(expand=True, fill='both', pady=10)

        self.load_items()

    def load_items(self):
        self.tree.delete(*self.tree.get_children())
        for item in self.items.find():
            self.tree.insert('', 'end', values=(
                item.get("nama", ""),
                item.get("kategori", ""),
                item.get("jumlah", 0),
                item.get("kondisi", "")
            ))

    def show_transactions(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()
        TransactionWindow(self.main_area, self.user_data)

    def show_categories(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()
        CategoryWindow(self.main_area)

    def show_reports(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()
        ReportWindow(self.main_area)

    def logout(self):
        self.destroy()
        self.parent.destroy()
        messagebox.showinfo("Logout", "Anda telah logout.")
