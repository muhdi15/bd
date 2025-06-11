import pymongo

from pymongo import *

#Buat koneksi untuk mongoDB

client= MongoClient("mongodb://localhost:27017/")
db = client["barang"]
collection = db['aset']


def totalData():
    total = collection.count_documents({})
    return total


def insert_barang(nama, kategori, stok, harga, kondisi):
    collection.insert_one({
        "nama" : nama,
        "kategori" : kategori,
        "stok" : int(stok),
        "harga" : int(harga),
        "kondisi" : kondisi
    })
    print("inserted Successfully")
    
def update_barang()


# nama = input("masukkan nama barang :")
# kategori = input("masukkan kategori barang :")
# stok = int(input("masukkan stok barang :"))
# harga = int(input("masukkan harga barang :"))
# kondisi = input("masukkan kondisi barang :")
# insert_barang(nama, kategori, stok, harga, kondisi)
