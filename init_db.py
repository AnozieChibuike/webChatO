import sqlite3

connectDb = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connectDb.executescript(f.read())

cur = connectDb.cursor()

cur.execute("INSERT INTO users (username,pass) VALUES (?,?)",
            ('admin','admin'))

connectDb.commit()
connectDb.close()
