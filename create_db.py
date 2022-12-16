from app import db, Task

print("Creating database")
db.create_all()
print("Database created.")