use wide_column_db

db.users.insertMany([
  { id: 1, name: "Derry", email: "derry@email.com", age: 25, city: "Majene" },
  { id: 2, name: "Sarah", email: "sarah@email.com", age: 22, city: "Makassar" },
  { id: 3, name: "Rizal", email: "rizal@email.com", age: 30, city: "Jakarta", phone: "08123456789" },
  { id: 4, name: "Intan", email: "intan@email.com", age: 27 },
  { id: 5, name: "Rudi", email: "rudi@email.com", age: 28, city: "Surabaya", isActive: true }
])
