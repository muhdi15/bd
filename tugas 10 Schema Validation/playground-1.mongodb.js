// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("barang");

db.runCommand({
  collMod: "aset",
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["nama", "kategori", "stok", "harga", "kondisi"],
      properties: {
        nama: {
          bsonType: "string",
          description: "Harus berupa string dan tidak boleh kosong"
        },
        kategori: {
          bsonType: "string",
          description: "Harus berupa string dan wajib ada"
        },
        stok: {
          bsonType: "int",
          minimum: 0,
          description: "Harus berupa bilangan bulat >= 0"
        },
        harga: {
          bsonType: "int",
          minimum: 0,
          description: "Harus berupa bilangan bulat >= 0"
        },
        kondisi: {
          enum: ["Baik", "Rusak", "Perlu Perbaikan"],
          description: "Hanya boleh salah satu dari: Baik, Rusak, Perlu Perbaikan"
        }
      }
    }
  },
  validationLevel: "strict",
  validationAction: "error"
})

