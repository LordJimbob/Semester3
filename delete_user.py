import sqlite3

db = sqlite3.connect("database.sqlite")
q = "DELETE FROM users WHERE id =?"
db.execute(q, ("03233f9d-3894-4081-8608-12ca05f9ecca",))
db.commit()
