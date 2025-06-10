// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("barang");

db.aset.aggregate([
  // 1. Menyaring hanya aset dengan kondisi "Baik"
  {
    $match: { kondisi: "Baik" }
  },
  
  // 2. Menambahkan field totalNilai (stok × harga) untuk setiap aset
  {
    $addFields: {
      totalNilai: { $multiply: ["$stok", "$harga"] }
    }
  },

  // 3. Mengelompokkan berdasarkan kategori, menghitung total stok per kategori, 
  // jumlah barang per kategori, dan total nilai aset per kategori
  {
    $group: {
      _id: "$kategori",
      totalStok: { $sum: "$stok" },           // Menghitung total stok per kategori
      jumlahBarang: { $sum: 1 },              // Menghitung jumlah barang per kategori
      nilaiAsetKategori: { $sum: "$totalNilai" } // Menghitung total nilai aset per kategori
    }
  }
])