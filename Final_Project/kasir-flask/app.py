from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'kasir-sederhana'

# Koneksi MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["kasir_db"]
barang_col = db["barang"]
transaksi_col = db["transaksi"]

# ----------------------
# ROUTES
# ----------------------

@app.route("/")
def index():
    total_barang = barang_col.count_documents({})
    total_transaksi = transaksi_col.count_documents({})
    total_pendapatan = sum(t['total'] for t in transaksi_col.find())
    return render_template("index.html",
                           total_barang=total_barang,
                           total_transaksi=total_transaksi,
                           total_pendapatan=total_pendapatan)

@app.route("/barang", methods=["GET", "POST"])
def barang():
    if request.method == "POST":
        nama = request.form["nama"]
        harga = int(request.form["harga"])
        stok = int(request.form["stok"])
        barang_col.insert_one({
            "nama": nama,
            "harga": harga,
            "stok": stok
        })
        flash("Barang berhasil ditambahkan!", "success")
        return redirect(url_for("barang"))

    daftar_barang = list(barang_col.find())
    return render_template("barang.html", barang=daftar_barang)

@app.route("/transaksi", methods=["GET", "POST"])
def transaksi():
    if request.method == "POST":
        barang_id = request.form["barang_id"]
        jumlah = int(request.form["jumlah"])
        barang = barang_col.find_one({"_id": ObjectId(barang_id)})

        if barang and barang["stok"] >= jumlah:
            total = barang["harga"] * jumlah
            barang_col.update_one(
                {"_id": ObjectId(barang_id)},
                {"$inc": {"stok": -jumlah}}
            )
            transaksi_col.insert_one({
                "nama_barang": barang["nama"],
                "harga": barang["harga"],
                "jumlah": jumlah,
                "total": total,
                "tanggal": datetime.now()
            })
            flash("Transaksi berhasil disimpan!", "success")
        else:
            flash("Stok tidak mencukupi!", "danger")

        return redirect(url_for("transaksi"))

    daftar_barang = list(barang_col.find())
    return render_template("transaksi.html", barang=daftar_barang)

@app.route("/histori")
def histori():
    data = list(transaksi_col.find().sort("tanggal", -1))
    return render_template("histori.html", transaksi=data)

# ----------------------
# Run App
# ----------------------

if __name__ == "__main__":
    app.run(debug=True)