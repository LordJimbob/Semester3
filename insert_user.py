import sqlite3
import uuid

id = str(uuid.uuid4())
print(id)
print(type(id))
db = sqlite3.connect("database.sqlite")
q = "INSERT INTO users VALUES(?, ?)"
db.execute(q, (id, "A"))
db.commit()
