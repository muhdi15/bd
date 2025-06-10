// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("barang");

db.aset.bulkWrite([
  // 1. Insert aset baru
  {
    insertOne: {
      document: {
        nama: "Meja Kantor",
        kategori: "Furniture",
        stok: 8,
        harga: 300000,
        kondisi: "Baik"
      }
    }
  },

  // 2. Update stok Kursi Kayu
  {
    updateOne: {
      filter: { nama: "Kursi Kayu" },
      update: { $inc: { stok: 5 } } // Tambah 5 stok
    }
  },

  // 3. Hapus aset yang kondisinya Rusak
  {
    deleteMany: {
      filter: { kondisi: "Rusak" }
    }
  },

  // 4. Ganti data Lemari Besi dengan data baru
  {
    replaceOne: {
      filter: { nama: "Lemari Besi" },
      replacement: {
        nama: "Lemari Besi Baja",
        kategori: "Penyimpanan",
        stok: 2,
        harga: 1200000,
        kondisi: "Baik"
      }
    }
  }
])

