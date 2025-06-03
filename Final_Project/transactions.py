# File: transactions.py

import tkinter as tk
from tkinter import ttk, messagebox
from db import get_db
from datetime import datetime

class TransactionWindow(ttk.Frame):
    def __init__(self, parent, user_data):
        super().__init__(parent)
        self.parent = parent
        self.user_data = user_data
        self.db = get_db()
        self.items_col = self.db['items']
        self.transactions_col = self.db['transactions']
        self.pack(fill='both', expand=True)

        self.create_widgets()
        self.load_transactions()

    def create_widgets(self):
        frm_top = ttk.Frame(self)
        frm_top.pack(fill='x', pady=5)

        ttk.Label(frm_top, text="Transaksi Barang Masuk/Keluar", font=('Segoe UI', 16)).pack(anchor='w', pady=5)

        # Pilih item
        ttk.Label(frm_top, text="Pilih Barang:").pack(anchor='w')
        self.item_combo = ttk.Combobox(frm_top, state='readonly')
        self.item_combo.pack(fill='x', pady=2)
        self.load_items()

        # Jenis transaksi
        ttk.Label(frm_top, text="Jenis Transaksi:").pack(anchor='w')
        self.trans_type = ttk.Combobox(frm_top, values=["Masuk", "Keluar"], state='readonly')
        self.trans_type.current(0)
        self.trans_type.pack(fill='x', pady=2)

        # Jumlah
        ttk.Label(frm_top, text="Jumlah:").pack(anchor='w')
        self.qty_entry = ttk.Entry(frm_top)
        self.qty_entry.pack(fill='x', pady=2)

        # Tombol submit
        btn_frame = ttk.Frame(frm_top)
        btn_frame.pack(fill='x', pady=10)
        ttk.Button(btn_frame, text="Submit", command=self.submit_transaction).pack(side='left')

        # Table histori transaksi
        self.tree = ttk.Treeview(self, columns=("Barang", "Jenis", "Jumlah", "Tanggal", "User"), show='headings', height=15)
        for col in ("Barang", "Jenis", "Jumlah", "Tanggal", "User"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(fill='both', expand=True, pady=10)

    def load_items(self):
        items = list(self.items_col.find())
        self.items = items
        self.item_combo['values'] = [item.get('nama', 'Unknown') for item in items]
        if items:
            self.item_combo.current(0)

    def load_transactions(self):
        self.tree.delete(*self.tree.get_children())
        transactions = self.transactions_col.find().sort("tanggal", -1)
        for t in transactions:
            self.tree.insert('', 'end', values=(
                t.get('nama_barang', ''),
                t.get('jenis', ''),
                t.get('jumlah', 0),
                t.get('tanggal').strftime("%Y-%m-%d %H:%M"),
                t.get('user', '')
            ))

    def submit_transaction(self):
        selected_index = self.item_combo.current()
        if selected_index < 0:
            messagebox.showerror("Error", "Pilih barang terlebih dahulu")
            return
        item = self.items[selected_index]
        jenis = self.trans_type.get()
        try:
            jumlah = int(self.qty_entry.get())
            if jumlah <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus angka positif")
            return

        # Update stok barang
        current_stock = item.get('jumlah', 0)
        if jenis == "Keluar" and jumlah > current_stock:
            messagebox.showerror("Error", "Stok tidak cukup untuk pengeluaran")
            return

        new_stock = current_stock + jumlah if jenis == "Masuk" else current_stock - jumlah

        self.items_col.update_one({"_id": item["_id"]}, {"$set": {"jumlah": new_stock}})

        # Simpan transaksi
        self.transactions_col.insert_one({
            "nama_barang": item.get('nama'),
            "jenis": jenis,
            "jumlah": jumlah,
            "tanggal": datetime.now(),
            "user": self.user_data['username']
        })

        messagebox.showinfo("Sukses", f"Transaksi {jenis} {jumlah} {item.get('nama')} berhasil")
        self.load_transactions()
        self.load_items()
        self.qty_entry.delete(0, 'end')
