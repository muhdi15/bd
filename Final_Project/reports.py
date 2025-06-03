# File: reports.py

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from db import get_db
import pandas as pd

class ReportWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.db = get_db()
        self.items_col = self.db['items']
        self.transactions_col = self.db['transactions']
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Laporan Inventaris", font=('Segoe UI', 16)).pack(anchor='w', pady=10)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill='x', pady=10)

        ttk.Button(btn_frame, text="Export Data Barang ke Excel", command=self.export_items).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Export Transaksi ke Excel", command=self.export_transactions).pack(side='left', padx=5)

        self.text_log = tk.Text(self, height=10, state='disabled')
        self.text_log.pack(fill='both', expand=True, pady=10)

    def export_items(self):
        data = list(self.items_col.find({}, {"_id":0}))
        if not data:
            messagebox.showwarning("Data Kosong", "Tidak ada data barang untuk diekspor.")
            return

        df = pd.DataFrame(data)
        filepath = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                filetypes=[("Excel files", "*.xlsx")],
                                                title="Simpan File Excel Data Barang")
        if filepath:
            df.to_excel(filepath, index=False)
            self.log(f"Data barang berhasil diekspor ke {filepath}")

    def export_transactions(self):
        data = list(self.transactions_col.find({}, {"_id":0}))
        if not data:
            messagebox.showwarning("Data Kosong", "Tidak ada data transaksi untuk diekspor.")
            return

        # Ubah tanggal ke string agar Excel friendly
        for d in data:
            if 'tanggal' in d and d['tanggal'] is not None:
                d['tanggal'] = d['tanggal'].strftime("%Y-%m-%d %H:%M:%S")

        df = pd.DataFrame(data)
        filepath = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                filetypes=[("Excel files", "*.xlsx")],
                                                title="Simpan File Excel Data Transaksi")
        if filepath:
            df.to_excel(filepath, index=False)
            self.log(f"Data transaksi berhasil diekspor ke {filepath}")

    def log(self, message):
        self.text_log.config(state='normal')
        self.text_log.insert('end', message + '\n')
        self.text_log.see('end')
        self.text_log.config(state='disabled')
