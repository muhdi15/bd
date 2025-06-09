use('barang')


// and
db.aset.find({
    $and:[
        {kategori: "Furniture"},
        {stok: {$gte: 8}}
    ]
})

// or
db.aset.find({
    $or:[
        {kategori: "Elektronik"},
        {kondisi: "Baik"}
    ]
})


// not
db.aset.find({
    stok: {$not: {$gte : 8}}
}
    
)

//not
db.aset.find({
    $nor:[
        {kondisi: "Rusak"},
        {stok: {$gte: 5}}
    ]
})
