// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("Tugas1");

// Find a document in a collection.
db.Mahasiswa.insertMany([
  {Nama: "A", NIM: "1234567890", Kelas: "A"},
  {Nama: "B", NIM: "1234567891", Kelas: "A"},
    {Nama: "C", NIM: "1234567892", Kelas: "A"},
    {Nama: "D", NIM: "1234567893", Kelas: "A"},
]);

db.Mahasiswa.find();


