# File: categories.py

import tkinter as tk
from tkinter import ttk, messagebox
from db import get_db

class CategoryWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.db = get_db()
        self.categories_col = self.db['categories']
        self.pack(fill='both', expand=True)
        self.create_widgets()
        self.load_categories()

    def create_widgets(self):
        ttk.Label(self, text="Manajemen Kategori", font=('Segoe UI', 16)).pack(anchor='w', pady=10)

        frm_input = ttk.Frame(self)
        frm_input.pack(fill='x', pady=5)

        ttk.Label(frm_input, text="Nama Kategori:").pack(side='left')
        self.entry_name = ttk.Entry(frm_input)
        self.entry_name.pack(side='left', padx=5, fill='x', expand=True)

        ttk.Button(frm_input, text="Tambah", command=self.add_category).pack(side='left', padx=5)

        # Treeview kategori
        self.tree = ttk.Treeview(self, columns=("Nama",), show='headings', height=15)
        self.tree.heading("Nama", text="Nama Kategori")
        self.tree.pack(fill='both', expand=True, pady=10)
        self.tree.bind("<Delete>", self.delete_category)

        ttk.Label(self, text="Pilih kategori lalu tekan tombol Delete pada keyboard untuk menghapus.").pack(anchor='w')

    def load_categories(self):
        self.tree.delete(*self.tree.get_children())
        for cat in self.categories_col.find():
            self.tree.insert('', 'end', iid=str(cat['_id']), values=(cat['name'],))

    def add_category(self):
        name = self.entry_name.get().strip()
        if not name:
            messagebox.showerror("Error", "Nama kategori tidak boleh kosong")
            return

        if self.categories_col.find_one({"name": name}):
            messagebox.showerror("Error", "Kategori sudah ada")
            return

        self.categories_col.insert_one({"name": name})
        self.entry_name.delete(0, 'end')
        self.load_categories()

    def delete_category(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        confirm = messagebox.askyesno("Konfirmasi", "Hapus kategori yang dipilih?")
        if confirm:
            self.categories_col.delete_one({"_id": self._to_objectid(selected[0])})
            self.load_categories()

    def _to_objectid(self, id_str):
        from bson.objectid import ObjectId
        return ObjectId(id_str)
