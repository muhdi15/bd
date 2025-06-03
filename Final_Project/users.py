from db import get_db

db = get_db()
users = db['users']

if users.count_documents({"username": "admin"}) == 0:
    users.insert_one({"username": "admin", "password": "admin123"})
    print("User admin dibuat dengan password admin123")
else:
    print("User admin sudah ada")
