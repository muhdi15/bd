
use("barang");

db.aset.find({ harga: { $gt: 2000000 } });                    // Harga > 2.000.000
db.aset.find({ harga: { $lt: 500000 } });                     // Harga < 500.000
db.aset.find({ stok: { $gte: 10 } });                         // Stok >= 10
db.aset.find({ stok: { $lte: 5 } });                          // Stok <= 5
db.aset.find({ kategori: { $eq: "Elektronik" } });            // Kategori = Elektronik
db.aset.find({ kondisi: { $ne: "Rusak" } });                  // Kondisi != Rusak
db.aset.find({ harga: { $gte: 1000000, $lte: 5000000 } });    // Harga antara 1jt - 5jt 