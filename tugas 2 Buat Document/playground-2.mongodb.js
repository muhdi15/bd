
const database = "TransportationDB";
const collection = "kendaraan";

use(database);
db.collection.insertOne({
    "nama": "Kendaraan",
    "jumlahRoda": 0,
    "kapasitasPenumpang": 0,
    "jenisBahanBakar": "Tidak Diketahui",
    "tahunProduksi": 0
});
db.collection.insertMany([
    {
        "nama": "Bus",
        "jumlahRoda": 6,
        "kapasitasPenumpang": 50,
        "jenisBahanBakar": "Solar",
        "tahunProduksi": 2015
    },
    {
        "nama": "Mobil",
        "jumlahRoda": 4,
        "kapasitasPenumpang": 5,
        "jenisBahanBakar": "Bensin",
        "tahunProduksi": 2020
    },
    {
        "nama": "Sepeda Motor",
        "jumlahRoda": 2,
        "kapasitasPenumpang": 2,
        "jenisBahanBakar": "Bensin",
        "tahunProduksi": 2018
    },
    {
        "nama": "Truk",
        "jumlahRoda": 10,
        "kapasitasPenumpang": 3,
        "jenisBahanBakar": "Solar",
        "tahunProduksi": 2017
    }
]);