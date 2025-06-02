// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("barang");

db.aset.insertOne({
    "nama": "Laptop",
    "jumlah": 10,
    "harga": 15000000,
    "tanggal_pembelian": new Date("2023-01-15"),
    "kondisi": "Baik"
});

db.aset.find();

db.aset.updateOne(
    { "nama": "Laptop" },
    { $set: { "jumlah": 8, "kondisi": "Sangat Baik" } }
);

db.aset.find();

