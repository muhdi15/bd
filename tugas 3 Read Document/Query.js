use('barang');


db.aset.insertMany([
    {nama: 'Kursi', jumlah: 10, harga: 50000, kategori: 'mebel'},
    {nama: 'Meja', jumlah: 5, harga: 150000, kategori: 'mebel'},    
    {nama: 'Laptop', jumlah: 3, harga: 10000000, kategori: 'elektronik'},
    {nama: 'Printer', jumlah: 2, harga: 2000000, kategori: 'elektronik'},
    {nama: 'Kipas Angin', jumlah: 4, harga: 300000, kategori: 'elektronik'},
]);

// db.aset.find();

db.aset.deleteMany({kategori: 'elektronik'});
db.aset.find();



