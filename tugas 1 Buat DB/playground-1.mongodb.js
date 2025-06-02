// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("Buku");

// Find a document in a collection.
db.buku.insertMany([
  {Nama_Buku: "Tak Tahan hati", harga: "10000", Kelas_Buku: "A"},
  {Nama_Buku: "Senandung", harga: "20000", Kelas_Buku: "A"},
  {Nama_Buku: "Harga_diri", harga: "30000", Kelas_Buku: "A"},
  {Nama_Buku: "Diam Yang berteriak", harga: "40000", Kelas_Buku: "A"},
]);

db.buku.find();


